/*
* @Author: gloomyline
* @Date:   2019-07-11 10:41:53
* @Last Modified by:   gloomyline
* @Last Modified time: 2019-07-12 17:18:12
*/
$(function () {
    function render_time() {
        return moment($(this).data('timestamp')).format('LLL');
    }

    $('[data-toggle="tooltip"]').tooltip({
        title: render_time
    })
});