(function () {
    function loadXMLDoc() {
        var xmlhttp;
        if (window.XMLHttpRequest) {
            xmlhttp = new XMLHttpRequest();
        }else {
            xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
        }
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState === 4 && xmlhttp.status === 200 ) {

            }
        };
        xmlhttp.open('post','url',true);
        xmlhttp.setRequestHeader('头名','头的值');
        xmlhttp.send('发送数据');
    }

    var inputs = s('.login_box_main input');

    inputs.forEach(function (value) {
        console.log(value.parentNode);
        value.onfocus = function () {
            value.parentNode.style.border = '1px solid #a2e790';
        };

        value.onblur = function () {
            value.parentNode.style.border = '1px solid #b6b6b6'
        }
    });
})();

