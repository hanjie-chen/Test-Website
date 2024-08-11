# Templates文件夹简介

我们把包含变量和运算逻辑的 HTML 或其他格式的文本叫做**模板**，执行这些变量替换和逻辑计算工作的过程被称为**渲染**，这个工作由模板渲染引擎——Jinja2 来完成。

按照默认的设置，Flask 会从程序实例所在模块同级目录的 templates 文件夹中寻找模板，我们的程序目前存储在项目根目录的 app.py 文件里

## 404.html

当用户试图查找服务器中没有的资源是，会发生404的报错。这个网页用于取代原来单调的404 Not Found 页面



## Base.html

对于模板内容重复的问题，Jinja2 提供了模板继承的支持。这个机制和 Python 类继承非常类似：我们可以定义一个父模板，一般会称之为基模板（base template）。基模板中包含完整的 HTML 结构和导航栏、页首、页脚等通用部分。在子模板里，我们可以使用 `extends` 标签来声明继承自某个基模板。

基模板中需要在实际的子模板中追加或重写的部分则可以定义成块（block）。块使用 `block` 标签创建， `{% block 块名称 %}` 作为开始标记，`{% endblock %}` 或 `{% endblock 块名称 %}` 作为结束标记。通过在子模板里定义一个同样名称的块，你可以向基模板的对应块位置追加或重写内容。

因为基模板会被所有其他页面模板继承，如果你在基模板中使用了某个变量，那么这个变量也需要使用模板上下文处理函数注入到模板里。

## Index.html

个人网站主页，主要参考来自https://www.bmpi.com（包括格式和内容） 用于简单介绍自己
考虑未来的feature并且使用Bootstrap5实现：
1. dark mode / light mode swithc
2. auto-scale in different screen

`<main class="d-flex flex-column min-vh-100">`: 使用 Bootstrap 的 `d-flex` 和 `flex-column` 类，将主内容设置为一个最小高度为 100vh 的弹性盒子。



导航栏navigation bar

- `<nav class="navbar navbar-expand-sm navbar-custom fixed-top">`: 使用 Bootstrap 的 `navbar` 类创建一个响应式导航栏，`fixed-top` 类固定在页面顶部，其中`navbar-custom`设置其高度
- `<div class="container">`: 使用 Bootstrap 的 `container` 类，确保导航栏中的内容居中对齐。
- `<span>`: 显示网站标题。
- `<div class="collapse navbar-collapse" id="mynavbar">`: 包含导航链接的容器，响应式时可以折叠。
- `<ul class="navbar-nav ms-auto">`: 使用 Bootstrap 的 `navbar-nav` 类创建导航链接列表，`ms-auto` 类将其右对齐。
- `<li class="nav-item">`: 每个导航项。
- `<a class="nav-link" href="{{ url_for('index') }}">`: 导航链接，使用 `nav-link` 类。



主内容 Main Content

- `<div class="main-content container-fluid flex-grow-1 d-flex align-items-center justify-content-center">`: 使用 Bootstrap 的 `container-fluid` 类创建一个全宽容器，`flex-grow-1` 类使其占据剩余空间，`d-flex` 类将其设置为弹性盒子，`align-items-center` 和 `justify-content-center` 类使内容居中对齐。
- `<div class="content-wrapper">`: 包含主内容的容器。
- `<div class="container text-center mb-4">`: 使用 Bootstrap 的 `container` 类和 `text-center` 类，使内容居中对齐，`mb-4` 类增加底部外边距。
- `<img alt="avatar" class="rounded" style="width: 8vw;" src="{{ url_for('static', filename='images/headavatar/head_avatar_problem.png') }}">`: 显示头像图片，使用 `rounded` 类使其圆角，`style` 属性设置宽度为 8vw。
- `<div class="content">`: 包含文本内容的容器。
- `<h5 class="mb-3">`: 使用 Bootstrap 的 `h5` 类创建标题，`mb-3` 类增加底部外边距。



页脚Footer

- `<footer class="footer-custom py-3 ">`: 使用自定义类 `footer-custom` 创建页脚，`py-3` 类增加上下内边距。
- `<div class="container text-center">`: 使用 Bootstrap 的 `container` 类和 `text-center` 类，使内容居中对齐。
- `<span>© 2024 for Plain Personal Website</span>`: 显示版权信息。