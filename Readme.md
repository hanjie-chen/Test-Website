# About the website

This is the Frontend website of my personal website. Lask time I try to develop frontend and backend in both, but actaully failed because I stuck in the backend database desing and deploy.



# About the requirements.txt

1. how the content be generated?

about the content in the `requirements.txt`, I generate by the command `pip3 freeze > requirements.txt`

2. how to use the file

use the command `pip install -r requirements.txt` to install the dependency of the requirements.



# LLM Prompt

我在搭建一个个人网站，使用python flask框架，前端采用Bootstrap5，目前正在搭建前端部分。这是我目前的项目目录结构

```powershell
E:.
│  .gitignore
│  app.py
│  Readme.md
│  requirements.txt
│
├─static
│  │  StaticOverivew.md
│  │  style.css
│  │
│  ├─bootstrap5
│  │  ├─css
│  │  │      bootstrap-grid.css
│  │  │      bootstrap-grid.css.map
│  │  │      bootstrap-grid.min.css
│  │  │      bootstrap-grid.min.css.map
│  │  │      bootstrap-grid.rtl.css
│  │  │      bootstrap-grid.rtl.css.map
│  │  │      bootstrap-grid.rtl.min.css
│  │  │      bootstrap-grid.rtl.min.css.map
│  │  │      bootstrap-reboot.css
│  │  │      bootstrap-reboot.css.map
│  │  │      bootstrap-reboot.min.css
│  │  │      bootstrap-reboot.min.css.map
│  │  │      bootstrap-reboot.rtl.css
│  │  │      bootstrap-reboot.rtl.css.map
│  │  │      bootstrap-reboot.rtl.min.css
│  │  │      bootstrap-reboot.rtl.min.css.map
│  │  │      bootstrap-utilities.css
│  │  │      bootstrap-utilities.css.map
│  │  │      bootstrap-utilities.min.css
│  │  │      bootstrap-utilities.min.css.map
│  │  │      bootstrap-utilities.rtl.css
│  │  │      bootstrap-utilities.rtl.css.map
│  │  │      bootstrap-utilities.rtl.min.css
│  │  │      bootstrap-utilities.rtl.min.css.map
│  │  │      bootstrap.css
│  │  │      bootstrap.css.map
│  │  │      bootstrap.min.css
│  │  │      bootstrap.min.css.map
│  │  │      bootstrap.rtl.css
│  │  │      bootstrap.rtl.css.map
│  │  │      bootstrap.rtl.min.css
│  │  │      bootstrap.rtl.min.css.map
│  │  │
│  │  └─js
│  │          bootstrap.bundle.js
│  │          bootstrap.bundle.js.map
│  │          bootstrap.bundle.min.js
│  │          bootstrap.bundle.min.js.map
│  │          bootstrap.esm.js
│  │          bootstrap.esm.js.map
│  │          bootstrap.esm.min.js
│  │          bootstrap.esm.min.js.map
│  │          bootstrap.js
│  │          bootstrap.js.map
│  │          bootstrap.min.js
│  │          bootstrap.min.js.map
│  │
│  ├─font
│  │  │  font.css
│  │  │
│  │  ├─JetBrainsMono
│  │  │      JetBrainsMono-Regular.ttf
│  │  │      JetBrainsMono-Regular.woff2
│  │  │
│  │  └─PingFangSC
│  │          PingFangSCRegular.ttf
│  │          PingFangSCRegular.woff2
│  │
│  ├─icon
│  │      favicon_point.ico
│  │      favicon_wind.ico
│  │
│  └─images
│      │  paimon.gif
│      │  shogun.gif
│      │
│      └─headavatar
│              head_avatar_oh.png
│              head_avatar_problem.png
│              head_avatar_think.png
│
└─templates
        404.html
        hello_world.html
        index.html
        TemplatesOverview.md
```
这是我现在正在编写index.html界面
```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plain Personal Website</title>
     <!-- 网站图标 -->
     <link rel="icon" href="/static/icon/favicon_point.ico" type="image/x-icon">


    <!-- Bootstrap 5 CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap5/css/bootstrap.min.css') }}">
    <!-- use the pointed font -->
    <link rel="stylesheet" href="{{ url_for('static', filename='font/font.css') }}">
    <!-- pointed body color -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css')}}">
   
</head>
<body class="body_background">
  <main>
    <nav>
      test
    </nav>
    
    <div class="container-fluid min-vh-100 d-flex align-items-center justify-content-center p-5">
          <div class="content-wrapper">
            <div class="content">
              <h5 class="mb-3">👋 hi, 我是翰杰, earth online的一名NPC</h5>
              <h5 class="mb-3">🎓 我是一名 emm…… 原神玩家（好吧，这么说是因为我不知道应该说什么）</h5>
              <h5 class="mb-3">💻 我正在使用 Python Flask 和 Bootstrap 5 构建个人网站前端部分</h5>
              <h5 class="mb-3">🌟 我对二次元充满热情，省流，宅男</h5>
              <h5 class="mb-3">🚀 我的长期目标是不工作，每天可以自由的支配时间，尝试自己感兴趣的事情</h5>
              <h5 class="mb-3">📫 联系我：<a href="mailto:hanjiechen@outlook.com">hanjie-chen@outlook.com</a></h5>
            </div>
          </div> 
    </div>

    <footer>
      test
    </footer>
    
  </main>
 
  <!-- Bootstrap 5 JS Bundle with Popper -->
  <script src="{{ url_for('static', filename='bootstrap5/js/bootstrap.bundle.min.js') }}"></script>
</body>
</html>
```
我想要达到下面这个网页的效果：
```

<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="author" content="马大伟">
<meta name="description" content="终身学习（认知杠杆）* 全栈技术（时间杠杆）* 投资理财（财务杠杆） =&gt; 被动收入（人生杠杆）">
<meta name="keywords" content="life,dev,trade,passive income,money,developer,Self-management,IT technology,investment transactions">
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@BMPI11">
<meta name="twitter:creator" content="@madawei2699">
<meta name="twitter:title" content="BMPI" />
<meta name="twitter:description" content />
<meta name="twitter:image" content="https://og.bmpi.dev/BMPI.png">
<meta property="og:title" content="BMPI" />
<meta property="og:description" content="终身学习（认知杠杆）* 全栈技术（时间杠杆）* 投资理财（财务杠杆） =&gt; 被动收入（人生杠杆）" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://www.bmpi.dev/" /><meta property="og:site_name" content="BMPI" />
<meta name="og:image" content="https://og.bmpi.dev/BMPI.png">
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Blog",
    "name": "BMPI.dev",
    "url": "https://www.bmpi.dev",
    "sameAs": [
      "https://twitter.com/madawei2699",
      "https://github.com/bmpi-dev",
      "https://t.me/s/bmpi365",
      "https://zhuanlan.zhihu.com/improve365"
    ]
  }
  </script>
<base href="https://www.bmpi.dev/">
<title>BMPI</title>
<link rel="canonical" href="https://www.bmpi.dev/">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css" integrity="sha256-l85OmPOjvil/SOvVt3HnSSjzF1TUMyT9eV0c2BzEGzU=" crossorigin="anonymous" />
<link rel="stylesheet" href="https://www.bmpi.dev/css/coder.min.93931ae707050b69c3bcbf6952e01a7b9a8f0aff2cdba79a762869af1aa23821.css" integrity="sha256-k5Ma5wcFC2nDvL9pUuAae5qPCv8s26eadihprxqiOCE=" crossorigin="anonymous" media="screen" />
<link rel="stylesheet" href="https://www.bmpi.dev/css/coder-dark.min.a2fdc25deb82b741f3a807e38508c2dea269fc900c2b37ee8af380d97ea4d7a8.css" integrity="sha256-ov3CXeuCt0HzqAfjhQjC3qJp/JAMKzfuivOA2X6k16g=" crossorigin="anonymous" media="screen" />
<link rel="stylesheet" href="https://www.bmpi.dev/css/main.css" />
<script src="https://www.bmpi.dev/js/lazysizes.min.js" async></script>
<script src="https://www.bmpi.dev/js/custom.js" async></script>
<link rel="apple-touch-icon" sizes="180x180" href="https://www.bmpi.dev/images/ico/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://www.bmpi.dev/images/ico/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://www.bmpi.dev/images/ico/favicon-16x16.png">
<link rel="manifest" href="https://www.bmpi.dev/images/ico/site.webmanifest">
<link rel="alternate" type="application/rss+xml" href="https://www.bmpi.dev/index.xml" title="BMPI" />
<meta name="generator" content="Hugo 0.83.1" />
<meta name="baidu-site-verification" content="TiReu51WyJ" />
<link rel="preload" href="https://www.bmpi.dev/scss/tagcloud.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://www.bmpi.dev/scss/tagcloud.css"></noscript>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/heti/0.9.4/heti.min.css">
<link rel="preload" href="https://cdnjs.cloudflare.com/ajax/libs/lxgw-wenkai-webfont/1.7.0/lxgwwenkai-regular.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/lxgw-wenkai-webfont/1.7.0/lxgwwenkai-regular.min.css"></noscript>
<link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script defer type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/3.0.0/pure-min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/pure/3.0.0/grids-responsive.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/heti/0.9.4/heti.min.css">
<link href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script async defer data-website-id="356d3289-e627-409c-a9d7-a272cf789f0b" src="https://umami.bmpi.dev/script.js"></script>
</head>
<body class="colorscheme-auto">
<main class="wrapper">
<nav class="navigation">
<section class="container">
<a id="site-title" class="navigation-title" href="https://www.bmpi.dev/">
BMPI
</a>
<input type="checkbox" id="menu-toggle" />
<label class="menu-button float-right" for="menu-toggle"><i class="fas fa-bars"></i></label>
<ul class="navigation-list">
<li class="navigation-item">
<a class="navigation-link" href="https://github.com/madawei2699">GitHub</a>
</li>
<li class="navigation-item">
<a class="navigation-link" href="https://twitter.com/madawei2699">Twitter</a>
</li>
<li class="navigation-item">
<a class="navigation-link" href="https://www.bmpi.dev/self/">学习</a>
</li>
<li class="navigation-item">
<a class="navigation-link" href="https://www.i365.tech/">技术</a>
</li>
<li class="navigation-item">
<a class="navigation-link" href="https://www.myinvestpilot.com/">投资</a>
</li>
<li class="navigation-item menu-separator">
<span>|</span>
</li>
<li class="navigation-item">
<a href="https://www.bmpi.dev/en/">English</a>
</li>
</ul>
</section>
</nav>
<div class="content">
<section class="container centered">
<div class="about">
<div style="margin:0 auto;text-align:left;line-height:4rem;">
👋 Hi, I'm Dawei Ma, a full-stack developer from Earth.<br>
🎯 I've written <span style="text-decoration:underline;">110</span> posts totaling <span style="text-decoration:underline;">399</span>K words in Chinese.<br>
🚩 My blog has been viewed over <span id="all-page-views" style="text-decoration:underline;"></span>K times by readers in <span id="site-run-days" style="text-decoration:underline;"></span> days.<br>
🔨 I'm building 📈 <a href="https://www.chat2invest.com">chat2invest.com</a> 💹 <a href="https://www.myinvestpilot.com/">myinvestpilot.com</a> 📚 <a href="https://www.myreader.io/">myreader.io</a>.<br>
🤑 I'm managing an <a href="https://www.myinvestpilot.com/portfolio?t=bmpi&p=被动收入">ETF portfolio</a> to build passive income.<br>
⛽️ I'm focused on achieving my long-term <a href="https://www.bmpi.dev/goal/">goals</a>.<br>
📬 Stay in touch by subscribing to my <a href="https://ld.i365.tech/newsletter/e0b379d3-0be0-4ae5-9fe2-cd972a667cdb">newsletter</a>.
</div>
</div>
</section>
</div>
<footer class="footer">
<div class="footer-taxonomy">
<div>
<a href="https://t.me/bmpi_group"> 电报 </a>
⚡️
<a href="https://discord.gg/S9mzJfqfKD"> Discord </a>
⚡️
<a href="https://www.bmpi.dev/money/guide-to-open-global-investment-account/"> 开户 </a>
⚡️
<a href="https://www.bmpi.dev/talk/"> 演讲 </a>
⚡️
<a href="/weeklies"> 周记 </a>
</div>
</div>
<section class="container">
© 2019 - 2024
</section>
</footer>
</main>
<div id="the-modal" class="modal">
<span class="the-modal-close">&times;</span>
<img class="modal-content" id="the-modal-img01">
</div>
<script>
      AOS.init({
        disable: 'mobile'
      });
    </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/TypewriterJS/2.21.0/core.min.js"></script>
<script>
    function setTyperWriterEffect() {
      var title = document.getElementById('site-title');

      var typewriter = new Typewriter(title, {
          loop: true,
          delay: 75,
          cursor: "",
      });

      typewriter
      .typeString('BMPI')
      .pauseFor(3000)
      .deleteChars(3)
      .typeString('uild My Personal Insights')
      .pauseFor(2000)
      .deleteChars(16)
      .typeString('rogramming Insights')
      .pauseFor(2000)
      .deleteChars(19)
      .typeString('assive Income')
      .pauseFor(2000)
      .start();
    }
    setTyperWriterEffect();
  </script>
</body>
</html>

```

