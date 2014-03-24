FuMou = typeof FuMou === 'undefined' ? {} : FuMou;

FuMou.util = {
    renderTemplate: function (source_id, target_id, context) {
        var template_text = document.getElementById(source_id).innerHTML;
        var compiled = _.template(template_text);
        
        document.getElementById(target_id).innerHTML = compiled(context);
    },
};
