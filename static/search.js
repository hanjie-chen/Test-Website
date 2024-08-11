document.addEventListener('keydown', function(event) {
  if (event.key === '/') {
    event.preventDefault(); // 阻止默认的行为，如页面搜索
    const searchBox = document.getElementById('searchBox');
    searchBox.classList.add('expanded');
    searchBox.focus();
  }
});

document.getElementById('searchBox').addEventListener('blur', function() {
  this.classList.remove('expanded');
});
