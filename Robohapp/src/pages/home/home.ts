import { MovementService, ShutdownService } from "./../../services";
import { Component, OnInit } from "@angular/core";
import { NavController } from "ionic-angular";
import { MovementEntity } from "../../entities";
import { Subject } from "rxjs/Subject";
import "rxjs/add/operator/distinctUntilChanged";

export interface IJoystick {
    deltaX: number;
    deltaY: number;
}

@Component({
    selector: "page-home",
    templateUrl: "home.html"
})
export class HomePage implements OnInit {

    private _movement: MovementEntity;
    private speedControl: Subject<number>;
    private directionControl: Subject<number>;
    public result: string;
    public wait: boolean = false;
    public status: boolean = false;

    get movement() {
        return this._movement;
    }
    set movenent(value: MovementEntity) {
        this._movement = value;
    }

    constructor(public navCtrl: NavController,
        private movementService: MovementService,
        private shutdownService: ShutdownService) {
        this._movement = MovementEntity.create();
        this.speedControl = new Subject<number>();
        this.directionControl = new Subject<number>();

    }

    public ngOnInit(): void {
        this.speedControl
            .asObservable()
            .distinctUntilChanged(compareDelta)
            .subscribe(speed => {
                this.movement.speed = speed;
                this.onChangeMove();
            });
        this.directionControl
            .asObservable()
            .distinctUntilChanged(compareDelta)
            .subscribe(direction => {
                this.movement.direction = direction;
                this.onChangeMove();
            });

        this.testConnection();
    }

    public onChangeDirection(event: IJoystick) {
        this.directionControl.next(this.filterValue(event.deltaX));
    }

    public onChangeSpeed(event: IJoystick) {
        this.speedControl.next(this.filterValue(event.deltaY));
    }

    private filterValue(value: number) {
        if (value > 100) {
            return 100;
        } else if (value < -100) {
            return -100;
        } else {
            return value;
        }
    }

    private testConnection() {
        this.movement.speed = 0;
        this.movement.direction = 0;
        this.onChangeMove();
    }

    private onChangeMove() {
        this.movementService.moveRoboh(this._movement).subscribe(data => {
            console.log(data);
            this.status = data.content;
        }, error => {
            console.log("The api is down!");
            this.status = false;
        });
    }

    public onShutdown() {
        this.shutdownService.shutdown().subscribe(data => {
            console.log(data);
            this.status = data.content;
        }, error => {
            console.log("The api is down!");
            this.status = false;
        });
    }

}

function compareDelta(prev: number, current: number) {
    if (Math.abs(current) >= 100 || current === 0) {
        return prev === current;
    } else {
        return Math.abs(prev - current) < 10;
    }
}
