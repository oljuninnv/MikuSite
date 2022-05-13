if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|BB|PlayBook|IEMobile|Windows Phone|Kindle|Silk|Opera Mini/i.test(navigator.userAgent)) {
    window.mobile = true;
}
else {
    window.mobile  = false;
}


new Vue({
    el: "#page",
    data: {
        mobile: window.mobile
    }
})