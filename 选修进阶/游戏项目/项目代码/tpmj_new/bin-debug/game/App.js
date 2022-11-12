var __reflect = (this && this.__reflect) || function (p, c, t) {
    p.__class__ = c, t ? t.push(c) : t = [c], p.__types__ = p.__types__ ? t.concat(p.__types__) : t;
};
var __extends = (this && this.__extends) || function (d, b) {
    for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p];
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
};
/**
 * root Module
 */
var Tpm;
(function (Tpm) {
    /**
     * game gate
     */
    var App = (function (_super) {
        __extends(App, _super);
        function App() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        /**启动框架*/
        App.prototype.startUp = function () {
            //注册Controller
            this.registerController(Tpm.LoginController.NAME, new Tpm.LoginController());
            this.registerController(Tpm.HallController.NAME, new Tpm.HallController());
            this.registerController(Tpm.GameController.NAME, new Tpm.GameController());
            //LoginController注册网络监听
            var loginController = App.getController(Tpm.LoginController.NAME);
            loginController.onRegister();
            //注册场景
            var sceneMag = App.SceneManager;
            sceneMag.register(Tpm.SceneConst.HallScene, Tpm.HallScene);
            sceneMag.register(Tpm.SceneConst.GameScene, Tpm.GameScene);
            sceneMag.register(Tpm.SceneConst.LoginScene, Tpm.LoginScene);
            //注册弹框
            var panelMag = App.PanelManager;
            panelMag.registerAll();
            //监听断线事件
            this.addEvent(Tpm.EventConst.SocketClose, this.onSocketClose, this);
            //读取配置
            App.GameConfig.init();
            // 跳过网络
            if (App.DataCenter.debugInfo.skipNet) {
                if (App.DataCenter.debugInfo.skipHall) {
                    App.SceneManager.runScene(Tpm.SceneConst.GameScene, this.getController(Tpm.GameController.NAME));
                }
                else {
                    App.SceneManager.runScene(Tpm.SceneConst.HallScene, this.getController(Tpm.HallController.NAME));
                }
            }
            else {
                App.SceneManager.runScene(Tpm.SceneConst.LoginScene, this.getController(Tpm.LoginController.NAME));
            }
        };
        App.prototype.onSocketClose = function () {
            App.PanelManager.open(Tpm.PanelConst.SocketClosePanel, false, null, null, false);
        };
        /**
         * 获取控制模块
         * @ctrlName 控制模块名
         * @return 控制模块
         */
        App.getController = function (ctrlName) {
            return App.getInstance().getController(ctrlName);
        };
        Object.defineProperty(App, "DataCenter", {
            /**数据中心*/
            get: function () {
                return Tpm.DataCenter.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "DeviceUtils", {
            /**设备工具类*/
            get: function () {
                return Tpm.DeviceUtils.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "StageUtils", {
            /**舞台工具类*/
            get: function () {
                return Tpm.StageUtils.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "ResUtils", {
            /**资源管理类*/
            get: function () {
                return Tpm.ResUtils.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "LayerManager", {
            /**图层管理类*/
            get: function () {
                return Tpm.LayerManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "SoundManager", {
            /**声音管理*/
            get: function () {
                return Tpm.SoundManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "PopUpManager", {
            /**弹框管理类*/
            get: function () {
                return Tpm.PopUpManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "MessageBoxManager", {
            /**提示框管理类*/
            get: function () {
                return Tpm.MessageBoxManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "EventManager", {
            /**事件管理类*/
            get: function () {
                return Tpm.EventMananger.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "LoadingLock", {
            /**加载等待动画*/
            get: function () {
                return Tpm.LoadingLock.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "PanelManager", {
            /**弹框管理类*/
            get: function () {
                return Tpm.PanelManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "SceneManager", {
            /**场景管理类*/
            get: function () {
                return Tpm.SceneManager.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "PlatformBridge", {
            /**平台交互类*/
            get: function () {
                return Tpm.PlatformBridge.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "gameSocket", {
            /**游戏Socket*/
            get: function () {
                return Tpm.GameSocket.getInstance().gameSocket;
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "httpSender", {
            /**WEB服务*/
            get: function () {
                return Tpm.HttpSender.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "LocalStorageUtil", {
            /**缓存管理 */
            get: function () {
                return Tpm.LocalStorageUtil.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "GameConfig", {
            /**缓存配置 */
            get: function () {
                return Tpm.StorageConfig.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        Object.defineProperty(App, "ArtConfig", {
            /**美术配置 */
            get: function () {
                return Tpm.ArtConfig.getInstance();
            },
            enumerable: true,
            configurable: true
        });
        return App;
    }(Tpm.BaseApp));
    Tpm.App = App;
    __reflect(App.prototype, "Tpm.App");
})(Tpm || (Tpm = {}));
//# sourceMappingURL=App.js.map