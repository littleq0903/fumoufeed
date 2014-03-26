FuMou = typeof FuMou === 'undefined' ? {} : FuMou;

FuMou.app = {
    // Views

    updateSubmitView: function () {
        FuMou.fb.getPersonalPosts(function(response){
            var posts = response.data;
            console.debug(posts);
            FuMou.util.renderTemplate("fm-template-submit-post", "fm-post-options", {
                posts: posts
            });
        });
    },

    updateFeedView: function () {

    },

    initFeedView: function () {
        this.updateFeedView();
    },

    initSubmitView: function () {
        // submit button
        $('#fm-submit-btn').click(function(e){
        
        });

        this.updateSubmitView();
    },

    // Utils
    loggedIn: function () {
        FuMou.fb.getProfile(function(response){
            var myName = response.name;

            $("#fb-username").html(myName);
            $("#submit-form-fbname").val(myName);
        
            $("body").addClass('loggedin').removeClass('loggedout');
        });
    },
    
    loggedOut: function () {
        $("body").addClass('loggedout').removeClass('loggedin');
    },

    switchPage: function (pageClass) {
        var allPageClasses = ['container-feed', 'container-submit'];
        var $body = $("body");

        allPageClasses.map(function(pc) {
            $body.removeClass(pc);
        });
        $body.addClass(pageClass);
    },

    
    
    // Entry point 
    init: function () {


        // function to init all things
        FuMou.app.initFeedView();
        FuMou.app.initSubmitView();

        this.switchPage('container-submit');
    }
}
