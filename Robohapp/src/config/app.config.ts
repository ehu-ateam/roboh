const HOST = "rpi";

export class AppConfig {
    public static get API_ENDPOINT(): string { return `http://${HOST}:8080/`; }

}
