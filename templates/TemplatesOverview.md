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