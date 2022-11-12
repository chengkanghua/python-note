module Tpm {
    export class GameSocket extends SingleClass {
        public gameSocket: ClientSocket;       //调度服务器

        public constructor() {
            super();
            this.gameSocket = new ClientSocket();
            this.gameSocket.name = "gameSocket";
        }
    }
}
