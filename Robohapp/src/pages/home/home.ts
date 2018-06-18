import { MovementService }  from "./../../services/movement.service";
import { Component }        from "@angular/core";
import { NavController }    from "ionic-angular";
import { MovementEntity }   from "../../entities";

export interface IJoystick {
    deltaX: number;
    deltaY: number;
}

@Component({
    selector: "page-home",
    templateUrl: "home.html"
})
export class HomePage {

    private _movement: MovementEntity;
    public result: string;
    public wait: boolean = false;

    get movement() {
        return this._movement;
    }
    set movenent(value: MovementEntity) {
        this._movement = value;
    }

    constructor(public navCtrl: NavController,
                private movementService: MovementService) {
        this._movement = MovementEntity.create();
    }

    public onChangeDirection(event: IJoystick) {
        if (!this.wait) {
            this._movement.direction = this.filtleValue(event.deltaX);
            this.onChangeMove();
        }
    }

    public onChangeSpeed(event: IJoystick) {
        if (!this.wait) {
            this._movement.speed = this.filtleValue(event.deltaY);
            this.onChangeMove();
        }
    }

    private filtleValue(value: number) {
        if (value > 100) {
            return 100;
        } else if (value < -100) {
            return -100;
        } else {
            return value;
        }
    }

    private onChangeMove() {
        this.wait = true;
        setTimeout(() => {
            this.movementService.moveRoboh(this._movement).subscribe(data => console.log(data));
            this.wait = false;
        }, 100);
    }
}
