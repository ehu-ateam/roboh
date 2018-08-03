// const HOST = "rpi";
const HOST = "rpi-dhcp";
// const HOST = "192.168.4.1";

export class AppConfig {
    public static get API_ENDPOINT(): string { return `http://${HOST}:8080/`; }
}
