import { HttpModule }               from "@angular/http";
import { BrowserModule }            from "@angular/platform-browser";
import { ErrorHandler,
         NgModule }                 from "@angular/core";
import { IonicApp,
         IonicErrorHandler,
         IonicModule }              from "ionic-angular";
import { SplashScreen }             from "@ionic-native/splash-screen";
import { StatusBar }                from "@ionic-native/status-bar";
import { MyApp }                    from "./app.component";
import { HomePage }                 from "../pages/home/home";
import { HttpClientModule,
         HttpClient }               from "@angular/common/http";
import { MovementService }          from "../services/movement.service";
import { ShutdownService }          from "../services/shutdown.service";
import { NgxVirtualJoystickModule } from "ngx-virtual-joystick";

@NgModule({
    declarations: [
        MyApp,
        HomePage
    ],
    imports: [
        BrowserModule,
        IonicModule.forRoot(MyApp),
        NgxVirtualJoystickModule.forRoot(),
        HttpClientModule,
        HttpModule
    ],
    bootstrap: [IonicApp],
    entryComponents: [
        MyApp,
        HomePage
    ],
    providers: [
        StatusBar,
        SplashScreen,
        {
            provide: ErrorHandler,
            useClass: IonicErrorHandler
        },
        HttpClient,
        MovementService,
        ShutdownService,
    ]
})
export class AppModule {}
