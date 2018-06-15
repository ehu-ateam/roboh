// const HOST = "rpi";
const HOST = "192.168.0.210";

export class AppConfig {
    public static get API_ENDPOINT(): string { return `http://${HOST}:8080/`; }

}
