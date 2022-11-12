module Tpm {
    export class BaseGameMod extends BaseUI {
        public constructor() {
            super();
        }

        /**对应Scene */
        public get gameScene(): GameScene {
            return <GameScene>this.parent;
        }

        /**对应的控制器 */
        public get ctrl(): GameController {
            return App.getController(GameController.NAME);
        }
    }
}
