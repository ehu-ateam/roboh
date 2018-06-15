import { MovementEntity }   from "./../entities";
import { AppConfig }        from "./../config/app.config";
import { Injectable }       from "@angular/core";
import { Http,
         Response }         from "@angular/http";
import  "rxjs/add/operator/map";

@Injectable()
export class MovementService {
    constructor( private http: Http ) { }

    public moveRoboh(movement: MovementEntity) {
        return this.http.post(AppConfig.API_ENDPOINT + "movement", movement).map((res: Response) => res.json());
    }
}
