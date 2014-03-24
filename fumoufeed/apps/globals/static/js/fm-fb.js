FuMou = typeof FuMou === 'undefined' ? {} : FuMou;


FuMou.fb = {
    // Configuration
    loginOptions: {
        scope: [
            'read_stream',
            ]
    },

    // Methods
    login: function (cb) {
        /*
         * cb: callback function
         */
        var cb = cb || function(){};

        var summaryLoginOptions = {
            scope: FuMou.fb.loginOptions.scope.join(','),
        };

        FB.login(cb, summaryLoginOptions);
    },

    getProfile: function (cb) {
        FB.api('/me', cb);
    },

    getSinglePost: function (fb_post_id, cb) {
        var innerCallback = function (response) {
            cb(response);
        };
        FB.api('/' + fb_post_id, innerCallback);
    },

    getPersonalPosts: function (cb) {
        FB.api('/me/posts', cb);
    }

};
