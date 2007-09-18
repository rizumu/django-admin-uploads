$(function(){
    $('textarea').each(function(){
        $(this).after('<iframe style="border:none; width:755px; height:210px;" src="/uploads/?textarea='+this.id+'"></iframe>');
    });
});
