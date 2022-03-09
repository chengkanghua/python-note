<template>
  <div class="_21bLU4 _3kbg6I">
   <Header></Header>
   <div class="_3VRLsv" role="main">
    <div class="_gp-ck">
     <section class="ouvJEz">
      <h1 class="_1RuRku">{{article.title}}</h1>
      <div class="rEsl9f">
       <div class="_2mYfmT">
        <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_13D2Eh" :src="article.user.avatar" alt="" /></a>
        <div style="margin-left: 8px;">
         <div class="_3U4Smb">
          <span class="FxYr8x"><a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer">{{article.user.nickname}}</a></span>
          <button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-if="article.is_follow==2" @click="follow_author(false)"><span>已关注</span></button>
          <button data-locale="zh-CN" type="button" class="_3kba3h _1OyPqC _3Mi9q9 _34692-" v-else-if="article.is_follow!=3" @click="follow_author(true)"><span>关注</span></button>
         </div>
         <div class="s-dsoj">
          <time>{{article.pub_date|dateformat}}</time>
          <span>字数 {{article.content.length}}</span>
          <span>阅读 {{article.read_count}}</span>
         </div>
        </div>
       </div>
      </div>
      <article class="_2rhmJa">
       <div class="image-package">
        <div class="image-container" style="max-width: 640px; max-height: 420px; background-color: transparent;">
         <div class="image-container-fill" style="padding-bottom: 65.63%;"></div>
         <div class="image-view" data-width="640" data-height="420">
          <img src="https://upload-images.jianshu.io/upload_images/18529254-f62fac0d998cff23?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp" />
         </div>
        </div>
        <div class="image-caption"></div>
       </div>
       <p>文/小鸟飞过</p>
       <p>罗曼&middot;罗兰说：“生活中最沉重的负担不是工作，而是无聊。”</p>
       <div class="image-package">
        <div class="image-container" style="max-width: 700px; max-height: 152px; background-color: transparent;">
         <div class="image-container-fill" style="padding-bottom: 14.069999999999999%;"></div>
         <div class="image-view" data-width="1080" data-height="152">
          <img src="http://upload-images.jianshu.io/upload_images/18529254-a932f0ad8fbd51bb?imageMogr2/auto-orient/strip|imageView2/2/w/1080/format/webp" />
         </div>
        </div>
        <div class="image-caption"></div>
       </div>
       <p><strong>废掉一个人最快的方法</strong></p>
       <p><strong>就是让他闲着</strong></p>
       <p>这段时间，综艺节目《妻子的浪漫旅行第三季3》正在热播，四对明星夫妻的相处模式曝光，也让观众更了解了曾经饱受争议的女人唐一菲。</p>
       <p>有人很喜欢她大大咧咧的女侠性格，有人为她叫屈，当然还是有人骂她，说她旧事重提。</p>
       <p>而我，则是觉得非常惋惜。</p>
       <p>唐一菲是中央戏剧学院表演系毕业，真正的科班出身。</p>
       <p>从2003年到2011年，基本保证每年都有作品，要么拍电视剧、要么拍电影，2008年出演新版《红楼梦》的秦可卿也是颇为动人。</p>
       <div class="image-package">
        <div class="image-container" style="max-width: 533px; max-height: 510px; background-color: transparent;">
         <div class="image-container-fill" style="padding-bottom: 95.67999999999999%;"></div>
         <div class="image-view" data-width="533" data-height="510">
          <img src="http://upload-images.jianshu.io/upload_images/18529254-d92ace292d78aecb?imageMogr2/auto-orient/strip|imageView2/2/w/533/format/webp" />
         </div>
        </div>
        <div class="image-caption"></div>
       </div>
       <p>可是自2012年结婚后，8年时间里，只拍了一部电视剧，就再也没了一点儿消息，仿佛整个人生都停滞了。</p>
       <p>她在《妻子3》中展现出的婚姻状态是非常可悲的。</p>
       <p>一喝酒，就是吐槽自己的人生被毁了。</p>
       <div class="image-package">
        <div class="image-container" style="max-width: 532px; max-height: 394px;">
         <div class="image-container-fill" style="padding-bottom: 74.06%;"></div>
         <div class="image-view" data-width="532" data-height="394">
          <img data-original-src="//upload-images.jianshu.io/upload_images/18529254-5f20af5bb10bfa12" data-original-width="532" data-original-height="394" data-original-format="image/jpeg" data-original-filesize="17915" data-image-index="3" style="cursor: zoom-in;" class="image-loading" />
         </div>
        </div>
        <div class="image-caption"></div>
       </div>
       <p>要么直接形容老公凌潇肃是缩头乌龟。</p>
       <div class="image-package">
        <div class="image-container" style="max-width: 506px; max-height: 360px;">
         <div class="image-container-fill" style="padding-bottom: 71.15%;"></div>
         <div class="image-view" data-width="506" data-height="360">
          <img data-original-src="//upload-images.jianshu.io/upload_images/18529254-f2478cdc59c7e193" data-original-width="506" data-original-height="360" data-original-format="image/jpeg" data-original-filesize="23772" data-image-index="4" style="cursor: zoom-in;" class="image-loading" />
         </div>
        </div>
        <div class="image-caption"></div>
       </div>
       <p>作者简介：小鸟飞过，富小书的人，富书专栏作者，写温暖的文字，传递美好的情感；本文首发富小书（ID：fxsfrc），你身边最好的闺蜜，富书2018重磅推出新书《好好生活》。</p>
       <p><strong>注：本文章图片来源网络，如有侵权，请联系删除。</strong></p>
      </article>
      <div></div>
      <div class="_1kCBjS">
       <div class="_18vaTa">
        <div class="_3BUZPB">
         <div class="_2Bo4Th" role="button" tabindex="-1" aria-label="给文章点赞">
          <i aria-label="ic-like" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-like"></use>
           </svg></i>
         </div>
         <span class="_1LOh_5" role="button" tabindex="-1" aria-label="查看点赞列表">8人点赞<i aria-label="icon: right" class="anticon anticon-right">
           <svg viewbox="64 64 896 896" focusable="false" class="" data-icon="right" width="1em" height="1em" fill="currentColor" aria-hidden="true">
            <path d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path>
           </svg></i></span>
        </div>
        <div class="_3BUZPB">
         <div class="_2Bo4Th" role="button" tabindex="-1">
          <i aria-label="ic-dislike" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-dislike"></use>
           </svg></i>
         </div>
        </div>
       </div>
       <div class="_18vaTa">
        <a class="_3BUZPB _1x1ok9 _1OhGeD" href="/nb/38290018" target="_blank" rel="noopener noreferrer"><i aria-label="ic-notebook" class="anticon">
          <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
           <use xlink:href="#ic-notebook"></use>
          </svg></i><span>随笔</span></a>
        <div class="_3BUZPB ant-dropdown-trigger">
         <div class="_2Bo4Th">
          <i aria-label="ic-others" class="anticon">
           <svg width="1em" height="1em" fill="currentColor" aria-hidden="true" focusable="false" class="">
            <use xlink:href="#ic-others"></use>
           </svg></i>
         </div>
        </div>
       </div>
      </div>
      <div class="_19DgIp" style="margin-top:24px;margin-bottom:24px"></div>
      <div class="_13lIbp">
       <div class="_191KSt">
        &quot;小礼物走一走，来简书关注我&quot;
       </div>
       <button type="button" class="_1OyPqC _3Mi9q9 _2WY0RL _1YbC5u" @click="is_show_reward_window=true"><span>赞赏支持</span></button>
       <span class="_3zdmIj">还没有人赞赏，支持一下</span>
      </div>
      <div class="d0hShY">
       <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_27NmgV" src="https://upload.jianshu.io/users/upload_avatars/18529254/.png?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp" alt="  " /></a>
       <div class="Uz-vZq">
        <div class="Cqpr1X">
         <a class="HC3FFO _1OhGeD" href="/u/a70487cda447" title="書酱" target="_blank" rel="noopener noreferrer">書酱</a>
         <span class="_2WEj6j" title="你读书的样子真好看。">你读书的样子真好看。</span>
        </div>
        <div class="lJvI3S">
         <span>总资产0</span>
         <span>共写了78.7W字</span>
         <span>获得6,072个赞</span>
         <span>共1,308个粉丝</span>
        </div>
       </div>
       <button data-locale="zh-CN" type="button" class="_1OyPqC _3Mi9q9"><span>关注</span></button>
      </div>
     </section>
     <div id="note-page-comment">
      <div class="lazyload-placeholder"></div>
     </div>
    </div>
    <aside class="_2OwGUo">
     <section class="_3Z3nHf">
      <div class="_3Oo-T1">
       <a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer"><img class="_3T9iJQ" src="https://upload.jianshu.io/users/upload_avatars/18529254/.png?imageMogr2/auto-orient/strip|imageView2/1/w/90/h/90/format/webp" alt="" /></a>
       <div class="_32ZTTG">
        <div class="_2O0T_w">
         <div class="_2v-h3G">
          <span class="_2vh4fr" title="書酱"><a class="_1OhGeD" href="/u/a70487cda447" target="_blank" rel="noopener noreferrer">書酱</a></span>
         </div>
         <button data-locale="zh-CN" type="button" class="tzrf9N _1OyPqC _3Mi9q9 _34692-"><span>关注</span></button>
        </div>
        <div class="_1pXc22">
         总资产0
        </div>
       </div>
      </div>
      <div class="_19DgIp"></div>
     </section>
     <div>
      <div class="">
       <section class="_3Z3nHf">
        <h3 class="QHRnq8 QxT4hD"><span>推荐阅读</span></h3>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="这些话没人告诉你，但必须知道的社会规则">
          <a class="_1-HJSV _1OhGeD" href="/p/a3e56a0559ff" target="_blank" rel="noopener noreferrer">这些话没人告诉你，但必须知道的社会规则</a>
         </div>
         <div class="_19haGh">
          阅读 5,837
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致">
          <a class="_1-HJSV _1OhGeD" href="/p/d2a3724e2839" target="_blank" rel="noopener noreferrer">浙大学霸最美笔记曝光：真正的牛人，都“变态”到了极致</a>
         </div>
         <div class="_19haGh">
          阅读 12,447
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="征服一个女人最好的方式：不是讨好她，而是懂得去折腾她">
          <a class="_1-HJSV _1OhGeD" href="/p/f6acf67f039b" target="_blank" rel="noopener noreferrer">征服一个女人最好的方式：不是讨好她，而是懂得去折腾她</a>
         </div>
         <div class="_19haGh">
          阅读 5,311
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="告别平庸的15个小方法">
          <a class="_1-HJSV _1OhGeD" href="/p/cff7eb6b232b" target="_blank" rel="noopener noreferrer">告别平庸的15个小方法</a>
         </div>
         <div class="_19haGh">
          阅读 7,040
         </div>
        </div>
        <div class="cuOxAY" role="listitem">
         <div class="_3L5YSq" title="轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧">
          <a class="_1-HJSV _1OhGeD" href="/p/2a0ca1729b4b" target="_blank" rel="noopener noreferrer">轻微抑郁的人，会说这3句“口头禅”，若你一个不占，偷着乐吧</a>
         </div>
         <div class="_19haGh">
          阅读 16,411
         </div>
        </div>
       </section>
      </div>
     </div>
    </aside>
   </div>
  <div class="_23ISFX-body" v-if="is_show_reward_window">
   <div class="_3uZ5OL">
    <div class="_2PLkjk">
     <img class="_2R1-48" src="https://upload.jianshu.io/users/upload_avatars/9602437/8fb37921-2e4f-42a7-8568-63f187c5721b.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/100/h/100/format/webp" alt="" />
     <div class="_2h5tnQ">
      给作者送糖
     </div>
    </div>
    <div class="_1-bCJJ">
     <div class="LMa6S_" :class="reward_money==item?'_1vONvL':''" @click="reward_money=item" v-for="item in reward_money_list">
      <span>{{item}}</span>
     </div>
    </div>
    <textarea class="_1yN79W" placeholder="给Ta留言..." v-model="reward_message"></textarea>
    <div class="_1_B577">
     选择支付方式
    </div>
    <div class="_1-bCJJ">
     <div class="LMa6S_ _3PA8BN" @click="reward_type=1" :class="reward_type==1?'_1vONvL':''">
      <span>支付宝</span>
     </div>
     <div class="LMa6S_ _3PA8BN" @click="reward_type=2" :class="reward_type==2?'_1vONvL':''">
      简书余额
     </div>
    </div>
    <button type="button" class="_3A-4KL _1OyPqC _3Mi9q9 _1YbC5u" @click="gotopay"><span>确认支付</span><span> ￥</span>{{reward_money}}</button>
   </div>
  </div>
   <Footer></Footer>
  </div>
</template>

<script>
    import Header from "./common/Header";
    import Footer from "./common/Footer";
    import '../../static/css/font-awesome/css/font-awesome.css';
    export default {
        name: "Article",
        data(){
          return {
             reward_money_list:[
                2,5,10,20,50
             ],
             reward_message: "", // 打赏的留言
             reward_money: 0, // 用户打赏金额
             reward_type: 1,  // 用户打赏的支付方式
             is_show_reward_window: false, // 是否显示文章打赏的窗口
             token: "",
             article:{
               content:"",
               user:{},
               collection:{},
             },
             article_id: 0,
             is_follow: false,
          }
        },
        components:{
          Header,
          Footer,
        },
        filters:{
          dateformat(date){
            date = new Date(date);
            return date.toLocaleDateString() + " " +date.toLocaleTimeString();
          }
        },
        created() {
          this.article_id = this.$route.params.id;
          this.token = this.get_login_user();
          this.get_article();
        },
        methods:{
           get_login_user(){
            // 获取登录用户
            return localStorage.user_token || sessionStorage.user_token;
          },
          get_article(){
            if(this.article_id<1){
              this.$message.error("参数有误！"); // 返回上一页
              return false;
            }

            let params = {};
            if(this.token){
              params = {
                Authorization: "jwt "+ this.token,
              }
            }

            this.$axios.get(`${this.$settings.Host}/article/${this.article_id}/`,{
              headers:params
            }).then(response=>{
              this.article = response.data;
            }).catch(error=>{
              this.$message.error("无法获取当前文章的内容！");
            })
          },
          gotopay(){
            // 发起请求，获取支付链接
            this.$axios.post(`${this.$settings.Host}/payments/alipay/`, {
                  "money": this.reward_money,
                  "article_id": this.article_id,
                  "type": this.reward_type,
                  "message": this.reward_message,
                },{
                    headers:{
                      Authorization: "jwt " + this.token
                    }
                }).then(response=>{
                  // 跳转到支付页面
                  this.$message.success("跳转支付页面中...请稍候")
                  setTimeout(()=>{
                    // 新建窗口打开
                    window.open(response.data,"_blank");
                    // 关闭打赏窗口
                    this.is_show_reward_window = false;
                  },2000);
                 }).catch(error=>{
                  this.$message.error("无法发起赞赏！");
                });
          },
          follow_author(opera){
             // 判断用户是否登录
            let self = this;　
            if(!this.token){
              this.$alert("对不起，您尚未登录，请登录后继续操作！","警告",{
                callback(){
                  self.$router.push("/user/login");
                }
              });
              return false;
            }

            if(opera){
                // 关注作者
                this.$axios.post(`${this.$settings.Host}/users/follow/`,{
                  author_id: this.article.user.id,
                },{
                  headers:{
                    Authorization: "jwt "+this.token,
                  }
                }).then(response=>{
                  this.article.is_follow = 2;
                }).catch(error=>{
                  this.$message.error("关注失败！请刷新页面以后重新操作！");
                });

            }else{
                // 取消关注
                this.$axios.delete(`${this.$settings.Host}/users/follow/`,{
                  params:{
                    author_id: this.article.user.id,
                  },
                  headers:{
                    Authorization: "jwt "+this.token,
                  }
                }).then(response=>{
                  this.article.is_follow = 1;

                }).catch(error=>{
                  this.$message.error("取消关注失败！请刷新页面以后重新操作！");
                });
            }
          }
        },
    }
</script>

<style scoped>
*,:after,:before {
	box-sizing: border-box
}
input,button{
  outline: 0;
}
a:hover {
	color: #fa9e87
}

a:active {
	color: #c75342
}

a:active,a:hover {
	text-decoration: none;
	outline: 0
}

a[disabled] {
	color: rgba(0,0,0,.25);
	cursor: not-allowed;
	pointer-events: none
}

img {
	vertical-align: middle;
	border-style: none
}

svg:not(:root) {
	overflow: hidden
}
[role=button],a,area,button,input:not([type=range]),label,select,summary,textarea {
	-ms-touch-action: manipulation;
	touch-action: manipulation
}

button,input,optgroup,select,textarea {
	margin: 0;
	color: inherit;
	font-size: inherit;
	font-family: inherit;
	line-height: inherit
}

button,input {
	overflow: visible
}

button,select {
	text-transform: none
}[type=reset],[type=submit],button,html [type=button] {
	-webkit-appearance: button
}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner {
	padding: 0;
	border-style: none
}

input[type=checkbox],input[type=radio] {
	-webkit-box-sizing: border-box;
	box-sizing: border-box;
	padding: 0
}

input[type=date],input[type=datetime-local],input[type=month],input[type=time] {
	-webkit-appearance: listbox
}

textarea {
	overflow: auto;
	resize: vertical
}

fieldset {
	min-width: 0;
	margin: 0;
	padding: 0;
	border: 0
}

legend {
	display: block;
	width: 100%;
	max-width: 100%;
	margin-bottom: .5em;
	padding: 0;
	color: inherit;
	font-size: 1.5em;
	line-height: inherit;
	white-space: normal
}

progress {
	vertical-align: baseline
}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button {
	height: auto
}[type=search] {
	outline-offset: -2px;
	-webkit-appearance: none
}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration {
	-webkit-appearance: none
}

::selection {
	color: #fff;
	background: #ec7259
}

.clearfix:after,.clearfix:before {
	content: ""
}

.anticon {
	display: inline-block;
	color: inherit;
	font-style: normal;
	line-height: 0;
	text-align: center;
	text-transform: none;
	vertical-align: -.125em;
	text-rendering: optimizeLegibility;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale
}

.anticon>* {
	line-height: 1
}

.anticon svg {
	display: inline-block
}

.anticon:before {
	display: none
}

.anticon[tabindex] {
	cursor: pointer
}



._3Vh8Z9-info ._3Vh8Z9-notice-content .anticon,._3Vh8Z9-loading ._3Vh8Z9-notice-content .anticon {
	color: #0681d0
}

._3Vh8Z9-success ._3Vh8Z9-notice-content .anticon {
	color: #42c02e
}

._3Vh8Z9-warning ._3Vh8Z9-notice-content .anticon {
	color: #fa0
}

._3Vh8Z9-error ._3Vh8Z9-notice-content .anticon {
	color: #f50
}

@keyframes _2mnC5S {
	0% {
		max-height: 150px;
		padding: 4px;
		opacity: 1
	}

	to {
		max-height: 0;
		padding: 0;
		opacity: 0
	}
}


.ant-popover-message>.anticon {
	position: absolute;
	top: 8px;
	color: #faad14;
	font-size: 14px
}

.ant-popover-buttons button {
	margin-left: 8px
}


._1OyPqC {
	position: relative;
	flex-shrink: 0;
	display: inline-flex;
	justify-content: center;
	align-items: center;
	border-radius: 50px;
	touch-action: manipulation;
	cursor: pointer;
	background-image: none;
	white-space: nowrap;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	transition: all .2s cubic-bezier(.645,.045,.355,1);
	font-size: 14px;
	padding: 4px 12px;
	color: #969696;
	background-color: #fff;
	border: 1px solid #999
}

._1OyPqC+._1OyPqC,._1OyPqC>.anticon+span,._1OyPqC>span+.anticon {
	margin-left: 8px
}

._1OyPqC:focus,._1OyPqC:hover {
	color: #7d7d7d;
	background-color: #fff;
	border-color: #999
}

._1OyPqC:active {
	color: #636363;
	background-color: #fff;
	border-color: #999
}

body.reader-night-mode ._1OyPqC {
	color: #b3b3b3;
	background-color: #3d3d3d;
	border-color: #999
}

body.reader-night-mode ._1OyPqC:focus,body.reader-night-mode ._1OyPqC:hover {
	color: #ccc;
	background-color: #3d3d3d;
	border-color: #999
}

body.reader-night-mode ._1OyPqC:active {
	color: #e6e6e6;
	background-color: #3d3d3d;
	border-color: #999
}

._3Mi9q9,._3Mi9q9[disabled]:hover {
	color: #ec7259;
	background-color: #fff;
	border-color: #ec7259
}

._3Mi9q9:focus,._3Mi9q9:hover {
	color: #ec7259;
	background-color: #fef8f7;
	border-color: #ec7259
}

._3Mi9q9:active {
	color: #ec7259;
	background-color: #fdf1ee;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9,body.reader-night-mode ._3Mi9q9[disabled]:hover {
	color: #ec7259;
	background-color: #3d3d3d;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9:focus,body.reader-night-mode ._3Mi9q9:hover {
	color: #ec7259;
	background-color: #46403f;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9:active {
	color: #ec7259;
	background-color: #4f4240;
	border-color: #ec7259
}


._3Mi9q9._1YbC5u,._3Mi9q9._1YbC5u[disabled]:hover {
	color: #fff;
	background-color: #ec7259;
	border-color: #ec7259
}

._3Mi9q9._1YbC5u:focus,._3Mi9q9._1YbC5u:hover {
	color: #fff;
	background-color: #ed7961;
	border-color: #ec7259
}

._3Mi9q9._1YbC5u:active {
	color: #fff;
	background-color: #ee806a;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u,body.reader-night-mode ._3Mi9q9._1YbC5u[disabled]:hover {
	color: #fff;
	background-color: #ec7259;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u:focus,body.reader-night-mode ._3Mi9q9._1YbC5u:hover {
	color: #fff;
	background-color: #ed7961;
	border-color: #ec7259
}

body.reader-night-mode ._3Mi9q9._1YbC5u:active {
	color: #fff;
	background-color: #ee806a;
	border-color: #ec7259
}

.ant-dropdown-menu-item>.anticon:first-child,.ant-dropdown-menu-submenu-title>.anticon:first-child {
	min-width: 12px;
	margin-right: 8px
}

.ant-dropdown-menu-item>a,.ant-dropdown-menu-submenu-title>a {
	display: block;
	margin: -5px -12px;
	padding: 5px 12px;
	color: rgba(0,0,0,.65);
	-webkit-transition: all .3s;
	transition: all .3s
}

.ant-btn>a:only-child {
	color: currentColor
}

.ant-btn>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn:focus>a:only-child,.ant-btn:hover>a:only-child {
	color: currentColor
}

.ant-btn:focus>a:only-child:after,.ant-btn:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn.active>a:only-child,.ant-btn:active>a:only-child {
	color: currentColor
}

.ant-btn.active>a:only-child:after,.ant-btn:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-disabled.active>a:only-child,.ant-btn-disabled:active>a:only-child,.ant-btn-disabled:focus>a:only-child,.ant-btn-disabled:hover>a:only-child,.ant-btn-disabled>a:only-child,.ant-btn.disabled.active>a:only-child,.ant-btn.disabled:active>a:only-child,.ant-btn.disabled:focus>a:only-child,.ant-btn.disabled:hover>a:only-child,.ant-btn.disabled>a:only-child,.ant-btn[disabled].active>a:only-child,.ant-btn[disabled]:active>a:only-child,.ant-btn[disabled]:focus>a:only-child,.ant-btn[disabled]:hover>a:only-child,.ant-btn[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-disabled.active>a:only-child:after,.ant-btn-disabled:active>a:only-child:after,.ant-btn-disabled:focus>a:only-child:after,.ant-btn-disabled:hover>a:only-child:after,.ant-btn-disabled>a:only-child:after,.ant-btn.disabled.active>a:only-child:after,.ant-btn.disabled:active>a:only-child:after,.ant-btn.disabled:focus>a:only-child:after,.ant-btn.disabled:hover>a:only-child:after,.ant-btn.disabled>a:only-child:after,.ant-btn[disabled].active>a:only-child:after,.ant-btn[disabled]:active>a:only-child:after,.ant-btn[disabled]:focus>a:only-child:after,.ant-btn[disabled]:hover>a:only-child:after,.ant-btn[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn>i,.ant-btn>span {
	display: inline-block;
	-webkit-transition: margin-left .3s cubic-bezier(.645,.045,.355,1);
	transition: margin-left .3s cubic-bezier(.645,.045,.355,1);
	pointer-events: none
}

.ant-btn-primary>a:only-child {
	color: currentColor
}

.ant-btn-primary>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-primary:focus>a:only-child,.ant-btn-primary:hover>a:only-child {
	color: currentColor
}

.ant-btn-primary:focus>a:only-child:after,.ant-btn-primary:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-primary.active>a:only-child,.ant-btn-primary:active>a:only-child {
	color: currentColor
}

.ant-btn-primary.active>a:only-child:after,.ant-btn-primary:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-primary-disabled.active>a:only-child,.ant-btn-primary-disabled:active>a:only-child,.ant-btn-primary-disabled:focus>a:only-child,.ant-btn-primary-disabled:hover>a:only-child,.ant-btn-primary-disabled>a:only-child,.ant-btn-primary.disabled.active>a:only-child,.ant-btn-primary.disabled:active>a:only-child,.ant-btn-primary.disabled:focus>a:only-child,.ant-btn-primary.disabled:hover>a:only-child,.ant-btn-primary.disabled>a:only-child,.ant-btn-primary[disabled].active>a:only-child,.ant-btn-primary[disabled]:active>a:only-child,.ant-btn-primary[disabled]:focus>a:only-child,.ant-btn-primary[disabled]:hover>a:only-child,.ant-btn-primary[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-primary-disabled.active>a:only-child:after,.ant-btn-primary-disabled:active>a:only-child:after,.ant-btn-primary-disabled:focus>a:only-child:after,.ant-btn-primary-disabled:hover>a:only-child:after,.ant-btn-primary-disabled>a:only-child:after,.ant-btn-primary.disabled.active>a:only-child:after,.ant-btn-primary.disabled:active>a:only-child:after,.ant-btn-primary.disabled:focus>a:only-child:after,.ant-btn-primary.disabled:hover>a:only-child:after,.ant-btn-primary.disabled>a:only-child:after,.ant-btn-primary[disabled].active>a:only-child:after,.ant-btn-primary[disabled]:active>a:only-child:after,.ant-btn-primary[disabled]:focus>a:only-child:after,.ant-btn-primary[disabled]:hover>a:only-child:after,.ant-btn-primary[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-ghost>a:only-child {
	color: currentColor
}

.ant-btn-ghost>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-ghost:focus>a:only-child,.ant-btn-ghost:hover>a:only-child {
	color: currentColor
}

.ant-btn-ghost:focus>a:only-child:after,.ant-btn-ghost:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-ghost.active>a:only-child,.ant-btn-ghost:active>a:only-child {
	color: currentColor
}

.ant-btn-ghost.active>a:only-child:after,.ant-btn-ghost:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-ghost-disabled.active>a:only-child,.ant-btn-ghost-disabled:active>a:only-child,.ant-btn-ghost-disabled:focus>a:only-child,.ant-btn-ghost-disabled:hover>a:only-child,.ant-btn-ghost-disabled>a:only-child,.ant-btn-ghost.disabled.active>a:only-child,.ant-btn-ghost.disabled:active>a:only-child,.ant-btn-ghost.disabled:focus>a:only-child,.ant-btn-ghost.disabled:hover>a:only-child,.ant-btn-ghost.disabled>a:only-child,.ant-btn-ghost[disabled].active>a:only-child,.ant-btn-ghost[disabled]:active>a:only-child,.ant-btn-ghost[disabled]:focus>a:only-child,.ant-btn-ghost[disabled]:hover>a:only-child,.ant-btn-ghost[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-ghost-disabled.active>a:only-child:after,.ant-btn-ghost-disabled:active>a:only-child:after,.ant-btn-ghost-disabled:focus>a:only-child:after,.ant-btn-ghost-disabled:hover>a:only-child:after,.ant-btn-ghost-disabled>a:only-child:after,.ant-btn-ghost.disabled.active>a:only-child:after,.ant-btn-ghost.disabled:active>a:only-child:after,.ant-btn-ghost.disabled:focus>a:only-child:after,.ant-btn-ghost.disabled:hover>a:only-child:after,.ant-btn-ghost.disabled>a:only-child:after,.ant-btn-ghost[disabled].active>a:only-child:after,.ant-btn-ghost[disabled]:active>a:only-child:after,.ant-btn-ghost[disabled]:focus>a:only-child:after,.ant-btn-ghost[disabled]:hover>a:only-child:after,.ant-btn-ghost[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-dashed>a:only-child {
	color: currentColor
}

.ant-btn-dashed>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-dashed:focus>a:only-child,.ant-btn-dashed:hover>a:only-child {
	color: currentColor
}

.ant-btn-dashed:focus>a:only-child:after,.ant-btn-dashed:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-dashed.active>a:only-child,.ant-btn-dashed:active>a:only-child {
	color: currentColor
}

.ant-btn-dashed.active>a:only-child:after,.ant-btn-dashed:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-dashed-disabled.active>a:only-child,.ant-btn-dashed-disabled:active>a:only-child,.ant-btn-dashed-disabled:focus>a:only-child,.ant-btn-dashed-disabled:hover>a:only-child,.ant-btn-dashed-disabled>a:only-child,.ant-btn-dashed.disabled.active>a:only-child,.ant-btn-dashed.disabled:active>a:only-child,.ant-btn-dashed.disabled:focus>a:only-child,.ant-btn-dashed.disabled:hover>a:only-child,.ant-btn-dashed.disabled>a:only-child,.ant-btn-dashed[disabled].active>a:only-child,.ant-btn-dashed[disabled]:active>a:only-child,.ant-btn-dashed[disabled]:focus>a:only-child,.ant-btn-dashed[disabled]:hover>a:only-child,.ant-btn-dashed[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-dashed-disabled.active>a:only-child:after,.ant-btn-dashed-disabled:active>a:only-child:after,.ant-btn-dashed-disabled:focus>a:only-child:after,.ant-btn-dashed-disabled:hover>a:only-child:after,.ant-btn-dashed-disabled>a:only-child:after,.ant-btn-dashed.disabled.active>a:only-child:after,.ant-btn-dashed.disabled:active>a:only-child:after,.ant-btn-dashed.disabled:focus>a:only-child:after,.ant-btn-dashed.disabled:hover>a:only-child:after,.ant-btn-dashed.disabled>a:only-child:after,.ant-btn-dashed[disabled].active>a:only-child:after,.ant-btn-dashed[disabled]:active>a:only-child:after,.ant-btn-dashed[disabled]:focus>a:only-child:after,.ant-btn-dashed[disabled]:hover>a:only-child:after,.ant-btn-dashed[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-danger>a:only-child {
	color: currentColor
}

.ant-btn-danger>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-danger:focus>a:only-child,.ant-btn-danger:hover>a:only-child {
	color: currentColor
}

.ant-btn-danger:focus>a:only-child:after,.ant-btn-danger:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-danger.active>a:only-child,.ant-btn-danger:active>a:only-child {
	color: currentColor
}

.ant-btn-danger.active>a:only-child:after,.ant-btn-danger:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-danger-disabled.active>a:only-child,.ant-btn-danger-disabled:active>a:only-child,.ant-btn-danger-disabled:focus>a:only-child,.ant-btn-danger-disabled:hover>a:only-child,.ant-btn-danger-disabled>a:only-child,.ant-btn-danger.disabled.active>a:only-child,.ant-btn-danger.disabled:active>a:only-child,.ant-btn-danger.disabled:focus>a:only-child,.ant-btn-danger.disabled:hover>a:only-child,.ant-btn-danger.disabled>a:only-child,.ant-btn-danger[disabled].active>a:only-child,.ant-btn-danger[disabled]:active>a:only-child,.ant-btn-danger[disabled]:focus>a:only-child,.ant-btn-danger[disabled]:hover>a:only-child,.ant-btn-danger[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-danger-disabled.active>a:only-child:after,.ant-btn-danger-disabled:active>a:only-child:after,.ant-btn-danger-disabled:focus>a:only-child:after,.ant-btn-danger-disabled:hover>a:only-child:after,.ant-btn-danger-disabled>a:only-child:after,.ant-btn-danger.disabled.active>a:only-child:after,.ant-btn-danger.disabled:active>a:only-child:after,.ant-btn-danger.disabled:focus>a:only-child:after,.ant-btn-danger.disabled:hover>a:only-child:after,.ant-btn-danger.disabled>a:only-child:after,.ant-btn-danger[disabled].active>a:only-child:after,.ant-btn-danger[disabled]:active>a:only-child:after,.ant-btn-danger[disabled]:focus>a:only-child:after,.ant-btn-danger[disabled]:hover>a:only-child:after,.ant-btn-danger[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-link>a:only-child {
	color: currentColor
}

.ant-btn-link>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-link:focus>a:only-child,.ant-btn-link:hover>a:only-child {
	color: currentColor
}

.ant-btn-link:focus>a:only-child:after,.ant-btn-link:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-link.active>a:only-child,.ant-btn-link:active>a:only-child {
	color: currentColor
}

.ant-btn-link.active>a:only-child:after,.ant-btn-link:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-link-disabled.active>a:only-child,.ant-btn-link-disabled:active>a:only-child,.ant-btn-link-disabled:focus>a:only-child,.ant-btn-link-disabled:hover>a:only-child,.ant-btn-link-disabled>a:only-child,.ant-btn-link.disabled.active>a:only-child,.ant-btn-link.disabled:active>a:only-child,.ant-btn-link.disabled:focus>a:only-child,.ant-btn-link.disabled:hover>a:only-child,.ant-btn-link.disabled>a:only-child,.ant-btn-link[disabled].active>a:only-child,.ant-btn-link[disabled]:active>a:only-child,.ant-btn-link[disabled]:focus>a:only-child,.ant-btn-link[disabled]:hover>a:only-child,.ant-btn-link[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-link-disabled.active>a:only-child:after,.ant-btn-link-disabled:active>a:only-child:after,.ant-btn-link-disabled:focus>a:only-child:after,.ant-btn-link-disabled:hover>a:only-child:after,.ant-btn-link-disabled>a:only-child:after,.ant-btn-link.disabled.active>a:only-child:after,.ant-btn-link.disabled:active>a:only-child:after,.ant-btn-link.disabled:focus>a:only-child:after,.ant-btn-link.disabled:hover>a:only-child:after,.ant-btn-link.disabled>a:only-child:after,.ant-btn-link[disabled].active>a:only-child:after,.ant-btn-link[disabled]:active>a:only-child:after,.ant-btn-link[disabled]:focus>a:only-child:after,.ant-btn-link[disabled]:hover>a:only-child:after,.ant-btn-link[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn .anticon {
	-webkit-transition: margin-left .3s cubic-bezier(.645,.045,.355,1);
	transition: margin-left .3s cubic-bezier(.645,.045,.355,1)
}

.ant-btn .anticon.anticon-minus>svg,.ant-btn .anticon.anticon-plus>svg {
	shape-rendering: optimizeSpeed
}


.ant-btn.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline):not(.ant-btn-icon-only) .anticon:not(:last-child) {
	margin-left: -14px
}

.ant-btn-sm.ant-btn-loading:not(.ant-btn-circle):not(.ant-btn-circle-outline):not(.ant-btn-icon-only) .anticon {
	margin-left: -17px
}

.ant-btn-group-sm>.ant-btn>.anticon,.ant-btn-group-sm>span>.ant-btn>.anticon {
	font-size: 14px
}

.ant-btn:active>span,.ant-btn:focus>span {
	position: relative
}

.ant-btn>.anticon+span,.ant-btn>span+.anticon {
	margin-left: 8px
}


.ant-btn-background-ghost.ant-btn-primary>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-primary:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary:hover>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-primary.active>a:only-child,.ant-btn-background-ghost.ant-btn-primary:active>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-primary-disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-primary-disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-primary-disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary-disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-primary-disabled>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-primary.disabled>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled].active>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:active>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:focus>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]:hover>a:only-child,.ant-btn-background-ghost.ant-btn-primary[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-primary-disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary-disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary-disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary-disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary-disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary.disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled].active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-primary[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-danger>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-danger:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger:hover>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-danger.active>a:only-child,.ant-btn-background-ghost.ant-btn-danger:active>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-danger-disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-danger-disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-danger-disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger-disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-danger-disabled>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-danger.disabled>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled].active>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:active>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:focus>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]:hover>a:only-child,.ant-btn-background-ghost.ant-btn-danger[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-danger-disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger-disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger-disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger-disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger-disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger.disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled].active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-danger[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-background-ghost.ant-btn-link>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-link>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}


.ant-btn-background-ghost.ant-btn-link:focus>a:only-child,.ant-btn-background-ghost.ant-btn-link:hover>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-link:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-link:hover>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-background-ghost.ant-btn-link.active>a:only-child,.ant-btn-background-ghost.ant-btn-link:active>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-link.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link:active>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-btn-background-ghost.ant-btn-link-disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-link-disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-link-disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-link-disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-link-disabled>a:only-child,.ant-btn-background-ghost.ant-btn-link.disabled.active>a:only-child,.ant-btn-background-ghost.ant-btn-link.disabled:active>a:only-child,.ant-btn-background-ghost.ant-btn-link.disabled:focus>a:only-child,.ant-btn-background-ghost.ant-btn-link.disabled:hover>a:only-child,.ant-btn-background-ghost.ant-btn-link.disabled>a:only-child,.ant-btn-background-ghost.ant-btn-link[disabled].active>a:only-child,.ant-btn-background-ghost.ant-btn-link[disabled]:active>a:only-child,.ant-btn-background-ghost.ant-btn-link[disabled]:focus>a:only-child,.ant-btn-background-ghost.ant-btn-link[disabled]:hover>a:only-child,.ant-btn-background-ghost.ant-btn-link[disabled]>a:only-child {
	color: currentColor
}

.ant-btn-background-ghost.ant-btn-link-disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link-disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link-disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-link-disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-link-disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-link.disabled.active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link.disabled:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link.disabled:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-link.disabled:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-link.disabled>a:only-child:after,.ant-btn-background-ghost.ant-btn-link[disabled].active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link[disabled]:active>a:only-child:after,.ant-btn-background-ghost.ant-btn-link[disabled]:focus>a:only-child:after,.ant-btn-background-ghost.ant-btn-link[disabled]:hover>a:only-child:after,.ant-btn-background-ghost.ant-btn-link[disabled]>a:only-child:after {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background: transparent;
	content: ""
}

.ant-menu ol,.ant-menu ul {
	margin: 0;
	padding: 0;
	list-style: none
}


.ant-menu-item>a {
	display: block;
	color: rgba(0,0,0,.65)
}

.ant-menu-item>a:hover {
	color: #ec7259
}

.ant-menu-item>a:before {
	position: absolute;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	background-color: transparent;
	content: ""
}

.ant-menu-item .anticon,.ant-menu-submenu-title .anticon {
	min-width: 14px;
	margin-right: 10px;
	font-size: 14px;
	-webkit-transition: font-size .15s cubic-bezier(.215,.61,.355,1),margin .3s cubic-bezier(.645,.045,.355,1);
	transition: font-size .15s cubic-bezier(.215,.61,.355,1),margin .3s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-item .anticon+span,.ant-menu-submenu-title .anticon+span {
	opacity: 1;
	-webkit-transition: opacity .3s cubic-bezier(.645,.045,.355,1),width .3s cubic-bezier(.645,.045,.355,1);
	transition: opacity .3s cubic-bezier(.645,.045,.355,1),width .3s cubic-bezier(.645,.045,.355,1)
}

.ant-menu-horizontal>.ant-menu-item>a {
	display: block;
	color: rgba(0,0,0,.65)
}

.ant-menu-horizontal>.ant-menu-item>a:hover {
	color: #ec7259
}

.ant-menu-horizontal>.ant-menu-item>a:before {
	bottom: -2px
}

.ant-menu-horizontal>.ant-menu-item-selected>a {
	color: #ec7259
}

.ant-menu-inline-collapsed-tooltip .anticon {
	display: none
}

.ant-menu-inline-collapsed-tooltip a {
	color: hsla(0,0%,100%,.85)
}

.ant-menu-item-disabled>a,.ant-menu-submenu-disabled>a {
	color: rgba(0,0,0,.25)!important;
	pointer-events: none
}

._1OhGeD,._1OhGeD:active,._1OhGeD:hover {
	color: inherit
}

.ant-radio-disabled+span {
	color: rgba(0,0,0,.25);
	cursor: not-allowed
}

span.ant-radio+* {
	padding-right: 8px;
	padding-left: 8px
}

._3tVfGA hr {
	margin: 16px 0;
	border: none;
	border-top: 1px solid #eee
}

body.reader-night-mode ._3tVfGA hr {
	border-color: #2f2f2f
}

.PY53UF:hover>i {
	visibility: visible;
	opacity: 1
}

.PY53UF>span {
	margin-right: 4px;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap
}

.PY53UF>i {
	font-size: 12px;
	visibility: hidden;
	opacity: 0
}


._3VRLsv {
	box-sizing: content-box;
	width: 1000px;
	padding-left: 16px;
	padding-right: 16px;
	margin-left: auto;
	margin-right: auto
}

._3Z3nHf,.ouvJEz {
	background-color: #fff;
	border-radius: 4px;
	margin-bottom: 10px
}

body.reader-night-mode ._3Z3nHf,body.reader-night-mode .ouvJEz {
	background-color: #3d3d3d
}

._3kbg6I {
	background-color: #f9f9f9
}

body.reader-night-mode ._3kbg6I {
	background-color: #2d2d2d
}

._3VRLsv {
	display: flex;
	justify-content: center;
	align-items: flex-start;
	min-height: calc(100vh - 66px);
	padding-top: 10px;
	font-size: 16px
}

._gp-ck {
	flex-shrink: 0;
	width: 730px;
	margin-bottom: 24px;
	margin-right: 10px
}

.ouvJEz {
	padding: 24px
}

._2OwGUo {
	flex-shrink: 0;
	width: 260px
}

._3Z3nHf {
	padding: 16px
}

.QxT4hD {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 16px;
	padding-left: 12px;
	border-left: 4px solid #ec7259;
	font-size: 18px;
	font-weight: 500;
	height: 20px;
	line-height: 20px
}

.nnghRR>p {
	margin-bottom: 0
}

.LtPwLP>div {
	min-height: 100px;
	flex-grow: 1
}

.LtPwLP img {
	width: 150px;
	height: 100px;
	border-radius: 4px;
	border: 1px solid #f2f2f2;
	flex-shrink: 0
}

._3nj4GN>span {
	margin-left: 8px;
	line-height: 20px
}

._3nj4GN .anticon {
	font-size: 22px
}

.rEsl9f {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 32px;
	font-size: 13px
}

.s-dsoj {
	display: flex;
	color: #969696
}

.s-dsoj>:not(:last-child) {
	margin-right: 10px
}

._1NDgW7 {
	color: #969696;
	flex-shrink: 0
}

._3tCVn5 {
	display: inline-flex;
	align-items: center;
	justify-content: center;
	color: #ec7259
}

._3tCVn5 i {
	margin-right: .5em
}

._2mYfmT {
	display: flex;
	align-items: center
}

._13D2Eh {
	display: block;
	border-radius: 50%;
	border: 1px solid #eee;
	min-width: 48px;
	min-height: 48px;
	width: 48px;
	height: 48px
}

body.reader-night-mode ._13D2Eh {
	border-color: #2f2f2f
}

._3U4Smb {
	display: flex;
	align-items: center;
	margin-bottom: 6px
}

.FxYr8x {
	font-size: 16px;
	font-weight: 500;
	margin-right: 8px
}

._3kba3h {
	padding: 2px 9px
}


._2rhmJa {
	font-weight: 400;
	line-height: 1.8;
	margin-bottom: 20px;
	user-select: none
}

._2rhmJa h1,._2rhmJa h2,._2rhmJa h3,._2rhmJa h4,._2rhmJa h5,._2rhmJa h6 {
	margin-bottom: 16px
}

._2rhmJa h1 {
	font-size: 26px
}

._2rhmJa h2 {
	font-size: 24px
}

._2rhmJa h3 {
	font-size: 22px
}

._2rhmJa h4 {
	font-size: 20px
}

._2rhmJa h5 {
	font-size: 18px
}

._2rhmJa h6 {
	font-size: 16px
}

._2rhmJa p {
	margin-bottom: 20px;
	word-break: break-word
}

._2rhmJa hr {
	margin: 0 0 20px;
	border: 0;
	border-top: 1px solid #eee!important
}

body.reader-night-mode ._2rhmJa hr {
	border-color: #2f2f2f!important
}

._2rhmJa blockquote {
	padding: 20px;
	background-color: #fafafa;
	border-left: 6px solid #e6e6e6;
	word-break: break-word;
	font-size: 16px;
	font-weight: normal;
	line-height: 30px;
	margin: 0 0 20px
}

body.reader-night-mode ._2rhmJa blockquote {
	background-color: #595959;
	border-color: #262626
}

._2rhmJa blockquote h1:last-child,._2rhmJa blockquote h2:last-child,._2rhmJa blockquote h3:last-child,._2rhmJa blockquote h4:last-child,._2rhmJa blockquote h5:last-child,._2rhmJa blockquote h6:last-child,._2rhmJa blockquote li:last-child,._2rhmJa blockquote ol:last-child,._2rhmJa blockquote p:last-child,._2rhmJa blockquote ul:last-child {
	margin-bottom: 0
}

._2rhmJa blockquote .image-package {
	width: 100%;
	margin-left: 0
}

._2rhmJa ol,._2rhmJa ul {
	word-break: break-word;
	margin: 0 0 20px 20px
}

._2rhmJa ol li,._2rhmJa ul li {
	line-height: 30px
}

._2rhmJa ol li ol,._2rhmJa ol li ul,._2rhmJa ul li ol,._2rhmJa ul li ul {
	margin-top: 16px
}

._2rhmJa ol {
	list-style-type: decimal
}

._2rhmJa ul {
	list-style-type: disc
}

._2rhmJa code {
	padding: 2px 4px;
	border: none;
	vertical-align: middle;
	white-space: pre-wrap
}

._2rhmJa :not(pre) code {
	color: #c7254e;
	background-color: #f2f2f2
}

body.reader-night-mode ._2rhmJa :not(pre) code {
	background-color: #262626
}


._2rhmJa pre[class*=language-] code,._2rhmJa pre code {
	padding: 0;
	background-color: transparent;
	color: inherit;
	white-space: pre;
	vertical-align: unset
}

._2rhmJa table {
	width: 100%;
	margin-bottom: 20px;
	border-collapse: collapse;
	border: 1px solid #eee;
	border-left: none;
	word-break: break-word
}

body.reader-night-mode ._2rhmJa table,body.reader-night-mode ._2rhmJa table td,body.reader-night-mode ._2rhmJa table th {
	border-color: #2f2f2f
}

._2rhmJa table td,._2rhmJa table th {
	padding: 8px;
	border: 1px solid #eee;
	line-height: 20px;
	vertical-align: middle
}

._2rhmJa table th {
	font-weight: bold
}

._2rhmJa table thead th {
	vertical-align: middle;
	text-align: inherit
}

._2rhmJa table tr:nth-of-type(2n) {
	background-color: hsla(0,0%,70.2%,.15)
}

._2rhmJa table .image-package {
	width: 100%;
	margin-left: 0
}

._2rhmJa img {
	max-width: 100%
}

._2rhmJa .image-package {
	width: 100%;
	margin: 0;
	padding-bottom: 25px;
	text-align: center;
	font-size: 0
}

._2rhmJa .image-package img {
	max-width: 100%;
	width: auto;
	height: auto;
	vertical-align: middle;
	border: 0
}

body.reader-night-mode ._2rhmJa .image-package img {
	opacity: .85
}

._2rhmJa .image-package .image-container {
	position: relative;
	z-index: 95;
	background-color: #e6e6e6;
	transition: background-color .1s linear;
	margin: 0 auto
}

body.reader-night-mode ._2rhmJa .image-package .image-container {
	background-color: #595959
}

._2rhmJa .image-package .image-container-fill {
	z-index: 90
}

._2rhmJa .image-package .image-container .image-view {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	overflow: hidden
}

._2rhmJa .image-package .image-container .image-view img.image-loading {
	opacity: .3
}

._2rhmJa .image-package .image-container .image-view img {
	transition: all .15s linear;
	z-index: 95;
	opacity: 1
}

._2rhmJa .image-package .image-caption {
	min-width: 20%;
	max-width: 80%;
	min-height: 43px;
	display: inline-block;
	padding: 10px;
	margin: 0 auto;
	border-bottom: 1px solid #eee;
	font-size: 13px;
	color: #999
}

._2rhmJa .image-package .image-caption:empty {
	display: none
}

body.reader-night-mode ._2rhmJa .image-package .image-caption {
	border-color: #2f2f2f
}

._2Lt-af>a {
	margin-left: .5em
}

._19DgIp {
	width: 100%;
	height: 1px;
	margin: 16px 0;
	background-color: #eee
}

body.reader-night-mode ._19DgIp {
	background-color: #2f2f2f
}


.ant-select,.ant-select ol,.ant-select ul {
	margin: 0;
	padding: 0;
	list-style: none
}

.ant-select>ul>li>a {
	padding: 0;
	background-color: #fff
}

.ant-empty-image img {
	height: 100%
}

.ant-empty-image svg {
	height: 100%;
	margin: auto
}


._1kCBjS {
	justify-content: space-between;
	font-size: 14px;
	color: #969696;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

._1kCBjS,._3BUZPB,._18vaTa {
	display: flex;
	align-items: center
}

._3BUZPB>span {
	margin-left: 8px
}

._3BUZPB:not(:last-child) {
	margin-right: 12px
}

._2Bo4Th {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 40px;
	height: 40px;
	color: #969696;
	border: 1px solid #eee;
	border-radius: 50%;
	font-size: 18px;
	cursor: pointer
}

body.reader-night-mode ._2Bo4Th {
	border-color: #2f2f2f
}


._1LOh_5 {
	cursor: pointer
}

._1LOh_5 .anticon {
	font-size: 12px
}

._1x1ok9 {
	cursor: pointer
}

._1x1ok9 .anticon {
	font-size: 16px
}

._1yN79W {
	background-color: #f2f2f2
}

._1yN79W:-ms-input-placeholder {
	color: #999
}

._1yN79W::-ms-input-placeholder {
	color: #999
}

._1yN79W::placeholder {
	color: #999
}

body.reader-night-mode ._1yN79W {
	background-color: #333
}

._3uZ5OL {
	text-align: center;
	padding: 48px 64px;
  ext-align: center;
  padding: 48px 64px;
  width: 50%;
  position: fixed;
  top: 0;
  height: 540px;
  border-radius: 5px;
  left: 0;
  right: 0;
  bottom: 0;
  background: #eee;
  z-index: 999;
  margin: auto;
}

._2PLkjk {
	display: flex;
	justify-content: center;
	align-items: center;
	margin-bottom: 24px
}

._2R1-48 {
	min-width: 50px;
	min-height: 50px;
	width: 50px;
	height: 50px;
	border-radius: 50%;
	border: 1px solid #eee
}

._2h5tnQ {
	font-size: 24px;
	font-weight: 500;
	margin-left: 16px
}

._1-bCJJ {
	flex-wrap: wrap
}

._1-bCJJ,.LMa6S_ {
	display: flex;
	justify-content: center
}

.LMa6S_ {
	align-items: center;
	width: 162.5px;
	height: 56px;
	font-size: 16px;
	color: #969696;
	margin-bottom: 12px;
	margin-right: 12px;
	border-radius: 10px;
	border: 1px solid #eee;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none
}

body.reader-night-mode .LMa6S_ {
	border-color: #2f2f2f
}


.LMa6S_>i {
	font-size: 20px
}

.LMa6S_>span {
	font-size: 28px;
	font-style: italic
}

.LMa6S_:nth-child(3n) {
	margin-right: 0
}

.LMa6S_:nth-last-child(-n+3) {
	margin-bottom: 0
}

.LMa6S_:last-child {
	margin-right: 0
}

._2ByDWa>span {
	font-size: 16px;
	font-style: normal;
	opacity: 1
}

._2ByDWa>input {
	position: absolute;
	top: 50%;
	left: 50%;
	width: 100%;
	height: 36px;
	margin: 0 auto;
	text-align: center;
	transform: translate(-50%,-50%);
	background-color: transparent;
	opacity: 0;
	cursor: pointer
}

._2ByDWa>input::-webkit-inner-spin-button,._2ByDWa>input::-webkit-outer-spin-button {
	display: none
}

._2ByDWa._1vONvL>span {
	opacity: 0
}

._2ByDWa._1vONvL>input {
	opacity: 1;
	cursor: text
}

._3PA8BN>i {
	font-size: 30px
}

._3PA8BN>span {
	font-size: 16px;
	font-style: normal;
	margin-left: 4px
}


._1yN79W {
	display: block;
	width: 100%;
	height: 80px;
	resize: none;
	margin-top: 12px;
	padding: 12px;
	border: none;
	border-radius: 10px
}

._1_B577 {
	font-size: 15px;
	margin: 12px 0
}

._3A-4KL {
	margin-top: 24px;
	font-size: 18px;
	font-weight: normal;
	padding: 10px 48px
}

.d0hShY {
	display: flex;
	align-items: center;
	background-color: #fafafa;
	border-radius: 4px;
	padding: 12px 16px
}

body.reader-night-mode .d0hShY {
	background-color: #333
}

._27NmgV {
	border-radius: 50%;
	border: 1px solid #eee;
	min-width: 50px;
	min-height: 50px;
	width: 50px;
	height: 50px
}

body.reader-night-mode ._27NmgV {
	border-color: #2f2f2f
}

.Uz-vZq {
	flex-grow: 1;
	margin: 0 12px;
	overflow: hidden
}

.Cqpr1X {
	display: flex;
	align-items: center;
	margin-bottom: 2px
}

.HC3FFO {
	flex-shrink: 0;
	font-size: 16px;
	font-weight: 500
}


._2WEj6j {
	font-size: 14px;
	color: #666;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap
}

.lJvI3S {
	font-size: 14px;
	color: #969696
}

.lJvI3S>span {
	margin-right: 12px
}

.lJvI3S>span:last-child {
	margin-right: 0
}

._3MbC71>span {
	margin-right: 6px
}


body.reader-night-mode .H4XBOO>img {
	border-color: #3d3d3d
}

._13lIbp {
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: 40px 0 32px
}

._191KSt {
	font-size: 16px;
	font-weight: 500;
	margin-bottom: 16px
}

._3zdmIj {
	color: #666;
	margin-top: 24px
}



._37OvKa>i {
	color: #ec7259;
	font-size: 20px;
	margin-right: 8px
}


._3S34Y_>img {
	width: 144px;
	height: 144px;
	margin-bottom: 12px
}

._2JdSds>span {
	margin-left: 2px;
	pointer-events: none
}

._3yPTTQ>i {
	font-size: 16px;
	margin-right: 4px
}

</style>
