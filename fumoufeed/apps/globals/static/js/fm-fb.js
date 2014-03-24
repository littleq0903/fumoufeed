'use strict';

FuMou = typeof FuMou === 'undefined' ? {} : FuMou;


FuMou.FB = {
    // Configuration
    loginOptions: {
        scope: [
            'read_stream',
            ]
    },

    // Methods

    loginFacebook: function (cb) {
        /*
         * cb: callback function
         * hasPopup: prompt to user to request permissions
         */
        hasPopup = hasPopup || false;

        var summaryLoginOptions = {
            scope: FuMou.FB.loginOptions.scope.join(','),
        };

        FB.login(cb, summaryLoginOptions);
    }


    
    
};
