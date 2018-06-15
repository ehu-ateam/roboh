
export class MovementEntity {
    public speed: number;
    public direction: number;

    public static create() {
        return {
            speed: 0,
            direction: 0
        };
    }
}
