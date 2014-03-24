FuMou = typeof FuMou === 'undefined' ? {} : FuMou;

FuMou.app = {
    // Views
    initFeedView: function () {},

    initSubmitView: function () {
        FuMou.fb.getPersonalPosts(function(response){
            var posts = response.data;
            console.debug(posts);
            FuMou.util.renderTemplate("fm-template-submit-post", "fm-post-options", {
                posts: posts
            });
        });
    },

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
    
    init: function () {
        // function to init all things
        FuMou.app.initFeedView();
        FuMou.app.initSubmitView();
    }
}
