import { MovementService }  from "./../../services/movement.service";
import { Component }        from "@angular/core";
import { NavController }    from "ionic-angular";

import { MovementEntity }   from "../../entities";


@Component({
    selector: "page-home",
    templateUrl: "home.html"
})
export class HomePage {

    private _movement: MovementEntity;

    public result: string;

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

    public onChangeMovement() {
        this.movementService.moveRoboh(this._movement).subscribe(data => console.log(data));
    }
}
