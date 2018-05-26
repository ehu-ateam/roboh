import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

import { HttpClient }   from "@angular/common/http"


@Component({
    selector: 'page-home',
    templateUrl: 'home.html'
})
export class HomePage {

    public power: number = 0;
    public direction: number = 0;

    public result: string;

    constructor(public navCtrl: NavController,
                private http: HttpClient) {

    }

    public test() {
        this.http.get("assets/config.json").subscribe((result) => {
            console.log(result)
            this.result = result["hello"];
        }); 
    }
}
