(function () {
    var search = document.querySelector('.search');
    var searchText = document.querySelector('.search input');
    var userButtons = s('.user button');
    // 设置搜索框获得焦点时变色
    searchText.onfocus = function () {
        search.style.border = '1px solid #a2e790';
    };
    // 搜索框失去焦点时恢复
    searchText.onblur = function () {
        search.style.border = '1px solid #b6b6b6';
    };

    userButtons.forEach(function (value) {
        // 鼠标移动到按钮上时变色
        value.onmouseover = function () {
            value.style.border = '1px solid #a2e790';
            value.style.color = '#a2e790';
        };
        // 鼠标移除时恢复颜色
        value.onmouseout = function () {
            value.style.border = '1px solid #b6b6b6';
            value.style.color = '#b6b6b6';
        }
    })


})();