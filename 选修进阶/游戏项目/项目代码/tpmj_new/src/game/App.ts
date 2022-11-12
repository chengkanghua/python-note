/**
 * root Module
 */
module Tpm {
    /**
     * game gate
     */
    export class App extends BaseApp {
        /**启动框架*/
        public startUp(): void {
            //注册Controller
            this.registerController(LoginController.NAME, new LoginController());
            this.registerController(HallController.NAME, new HallController());
            this.registerController(GameController.NAME, new GameController());

            //LoginController注册网络监听
            var loginController:LoginController = App.getController(LoginController.NAME);
            loginController.onRegister();

            //注册场景
            var sceneMag: SceneManager = App.SceneManager;
            sceneMag.register(SceneConst.HallScene, HallScene);
            sceneMag.register(SceneConst.GameScene, GameScene);
            sceneMag.register(SceneConst.LoginScene, LoginScene);

            //注册弹框
            var panelMag: PanelManager = App.PanelManager;
            panelMag.registerAll();

            //监听断线事件
            this.addEvent(EventConst.SocketClose, this.onSocketClose, this);

            //读取配置
            App.GameConfig.init();

            // 跳过网络
            if (App.DataCenter.debugInfo.skipNet) {
                if (App.DataCenter.debugInfo.skipHall) {
                    App.SceneManager.runScene(SceneConst.GameScene, this.getController(GameController.NAME));
                }
                else {
                    App.SceneManager.runScene(SceneConst.HallScene, this.getController(HallController.NAME));
                }
            }
            // 连接网络
            else {
                App.SceneManager.runScene(SceneConst.LoginScene, this.getController(LoginController.NAME));
                
                // var loginCtr: LoginController = this.getController(LoginController.NAME);
                // loginCtr.loginGate();
            }
        }

        private onSocketClose() {
            App.PanelManager.open(PanelConst.SocketClosePanel, false, null, null, false);
        }

        /**
         * 获取控制模块
         * @ctrlName 控制模块名
         * @return 控制模块
         */
        public static getController(ctrlName: string) {
            return App.getInstance().getController(ctrlName);
        }

        /**数据中心*/
        public static get DataCenter(): DataCenter {
            return DataCenter.getInstance();
        }

        /**设备工具类*/
        public static get DeviceUtils(): DeviceUtils {
            return DeviceUtils.getInstance();
        }

        /**舞台工具类*/
        public static get StageUtils(): StageUtils {
            return StageUtils.getInstance();
        }

        /**资源管理类*/
        public static get ResUtils(): ResUtils {
            return ResUtils.getInstance();
        }

        /**图层管理类*/
        public static get LayerManager(): LayerManager {
            return LayerManager.getInstance();
        }

        /**声音管理*/
        public static get SoundManager(): SoundManager {
            return SoundManager.getInstance();
        }

        /**弹框管理类*/
        public static get PopUpManager(): PopUpManager {
            return PopUpManager.getInstance();
        }
           /**提示框管理类*/
        public static get MessageBoxManager(): MessageBoxManager {
            return MessageBoxManager.getInstance();
        }

        /**事件管理类*/
        public static get EventManager(): EventMananger {
            return EventMananger.getInstance();
        }

        /**加载等待动画*/
        public static get LoadingLock(): LoadingLock {
            return LoadingLock.getInstance();
        }

        /**弹框管理类*/
        public static get PanelManager(): PanelManager {
            return PanelManager.getInstance();
        }

        /**场景管理类*/
        public static get SceneManager(): SceneManager {
            return SceneManager.getInstance();
        }

        /**平台交互类*/
        public static get PlatformBridge(): PlatformBridge {
            return PlatformBridge.getInstance();
        }

        /**游戏Socket*/
        public static get gameSocket(): ClientSocket {
            return GameSocket.getInstance().gameSocket;
        }
        /**WEB服务*/
        public static get httpSender(): HttpSender {
            return HttpSender.getInstance();
        }

        /**缓存管理 */
        public static get LocalStorageUtil(): LocalStorageUtil {
            return LocalStorageUtil.getInstance();
        }

        /**缓存配置 */
        public static get GameConfig(): StorageConfig {
            return StorageConfig.getInstance();
        }

        /**美术配置 */
        public static get ArtConfig(): ArtConfig {
            return ArtConfig.getInstance();
        }
    }
}
