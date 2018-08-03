import { AppConfig }        from "./../config/app.config";
import { Injectable }       from "@angular/core";
import { Http,
         Response }         from "@angular/http";
import  "rxjs/add/operator/map";

@Injectable()
export class ShutdownService {
    constructor( private http: Http ) { }

    public shutdown() {
        return this.http.get(AppConfig.API_ENDPOINT + "shutdown").map((res: Response) => res.json());
    }
}
