# Static文件夹简介

静态文件（static files）和我们的模板概念相反，指的是内容不需要动态生成的文件。比如图片、CSS 文件和 JavaScript 脚本等。

在 HTML 文件里，引入这些静态文件需要给出资源所在的 URL。为了更加灵活，这些文件的 URL 可以通过 Flask 提供的 `url_for()` 函数来生成。在 Python 脚本里，`url_for()` 函数需要从 `flask` 包中导入，而在模板中则可以直接使用，因为 Flask 把一些常用的函数和对象添加到了模板上下文（环境）里。

在 Flask 中，我们需要创建一个 static 文件夹来保存静态文件，它应该和程序模块、templates 文件夹在同一目录层级

其中favicon_wind.ico图标是网站的图标

## CSS框架:Bootstrap5

决定了使用Bootstrap来弄CSS完成好看的网站搭建，适合我这种一个人搭建的网站。发现有两种方式来使用bootstrap，一个是使用CDN链接的方式，让其去加载网络上面的bootstrap文件，一个是本地下载bootstrap文件。当然以学习为目的来使用bootstrap，我选择将其下载到本地上面。

> 通过在HTML中使用CDN链接的方式使用Bootstrap和使用自己在本地下载的Bootstrap文件相比，主要区别在于：
>
> 1. 下载速度：使用CDN链接可以节省您下载和部署Bootstrap的时间和成本，因为浏览器会从CDN服务器上获取所需的CSS样式和JavaScript组件。而如果您使用本地下载的Bootstrap文件，则需要等待文件下载完毕并将其放置到正确的目录下，才能开始使用。
>
> 2. 可靠性：如果您使用CDN链接，则可以确保您的网站每次都使用最新版本的Bootstrap库，而不必担心您的本地文件是否过时或受到漏洞攻击。同时，由于CDN服务器分布在全球各地，因此您的用户可以更快地加载您的网站，提高用户体验。
>
> 3. 网络连接：如果您使用CDN链接，则需要访问外部服务器来获取Bootstrap文件，这意味着您的网站的可用性和性能可能会受到网络状况的影响。如果您使用本地下载的Bootstrap文件，则无需依赖网络连接，因此可以更加可靠和稳定。
>
> 总的来说，使用CDN链接的方式更加方便和快捷，但是使用本地下载的Bootstrap文件则更加稳定和可控。具体选择取决于您的实际需求和环境。

### Bootstrap-5.3.0

将下载的bootstrap压缩包解压到static文件夹下面，即可使用bootstrap5。包含如下文件

```shell
bootstrap5/
├── css/
│   ├── bootstrap-grid.css
│   ├── bootstrap-grid.css.map
│   ├── bootstrap-grid.min.css
│   ├── bootstrap-grid.min.css.map
│   ├── bootstrap-grid.rtl.css
│   ├── bootstrap-grid.rtl.css.map
│   ├── bootstrap-grid.rtl.min.css
│   ├── bootstrap-grid.rtl.min.css.map
│   ├── bootstrap-reboot.css
│   ├── bootstrap-reboot.css.map
│   ├── bootstrap-reboot.min.css
│   ├── bootstrap-reboot.min.css.map
│   ├── bootstrap-reboot.rtl.css
│   ├── bootstrap-reboot.rtl.css.map
│   ├── bootstrap-reboot.rtl.min.css
│   ├── bootstrap-reboot.rtl.min.css.map
│   ├── bootstrap-utilities.css
│   ├── bootstrap-utilities.css.map
│   ├── bootstrap-utilities.min.css
│   ├── bootstrap-utilities.min.css.map
│   ├── bootstrap-utilities.rtl.css
│   ├── bootstrap-utilities.rtl.css.map
│   ├── bootstrap-utilities.rtl.min.css
│   ├── bootstrap-utilities.rtl.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   ├── bootstrap.min.css.map
│   ├── bootstrap.rtl.css
│   ├── bootstrap.rtl.css.map
│   ├── bootstrap.rtl.min.css
│   └── bootstrap.rtl.min.css.map
└── js/
    ├── bootstrap.bundle.js
    ├── bootstrap.bundle.js.map
    ├── bootstrap.bundle.min.js
    ├── bootstrap.bundle.min.js.map
    ├── bootstrap.esm.js
    ├── bootstrap.esm.js.map
    ├── bootstrap.esm.min.js
    ├── bootstrap.esm.min.js.map
    ├── bootstrap.js
    ├── bootstrap.js.map
    ├── bootstrap.min.js
    └── bootstrap.min.js.map

```



## 字体Font

中文使用苹方简体`PingFangSC`英文使用Jetbrain开发的IDE字体`Jetbrain Mono`并且提供2种格式的加载方式，让浏览器自行选择。
