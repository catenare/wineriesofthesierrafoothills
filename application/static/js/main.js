// require.config({
//     baseUrl: 'static/js/lib',
//     paths: {
//         bootstrap: 'bootstrap',
//         gallery: '../apps/gallery',
//         hammerjs: 'hammer',
//         'bootstrap-sass': '../components/bootstrap-sass/assets/javascripts/bootstrap',
//         bower: '../components/bower/atom-full-compiled',
//         fastclick: '../components/fastclick/lib/fastclick',
//         install: '../components/install/detect-zoom',
//         jquery: '../components/jquery/dist/jquery',
//         'jquery-hammerjs': '../components/jquery-hammerjs/jquery.hammer',
//         'jquery-ui': '../components/jquery-ui/jquery-ui',
//         'jquery.easing': '../components/jquery.easing/js/jquery.easing',
//         'requirejs-google-analytics': '../components/requirejs-google-analytics/dist/GoogleAnalytics'
//     },
//     shim: {
//         bootstrap: {
//             deps: [
//                 'jquery'
//             ]
//         }
//     },
//     packages: [
//
//     ]
// });
require.config({
	    baseUrl: 'static/js/lib',
	    paths: {
	        bootstrap: 'bootstrap',
	        gallery: '../apps/gallery',
	        hammerjs: 'hammer',
	    },
	    shim : {
	        "bootstrap" : { "deps" :["jquery"] }
    },
});

require(["jquery","gallery","bootstrap"], function($,Gallery,Bootstrap){

        Gallery.preview();

        $('body').scrollspy({ target: '#navbar-scroll', offset: 10 });

        $('#navbar-scroll').on('activate.bs.scrollspy', function (e) {
        });

        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-66494005-1', 'auto');
        ga('send', 'pageview');
});
