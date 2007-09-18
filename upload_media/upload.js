function insertAtCursor(myField, myValue) {
    //IE support
    if (document.selection) {
        myField.focus();
        sel = document.selection.createRange();
        sel.text = myValue;
    }
    //MOZILLA/NETSCAPE support
    else if (myField.selectionStart || myField.selectionStart == '0') {
        var startPos = myField.selectionStart;
        var endPos = myField.selectionEnd;
        myField.value = myField.value.substring(0, startPos)
        + myValue
        + myField.value.substring(endPos, myField.value.length);
    } else {
        myField.value += myValue;
    }
}

//Django js function
function showAddAnotherPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^add_/, '');
    name = name.replace(/\./g, '___');
    href = triggeringLink.href
    if (href.indexOf('?') == -1) {
        href += '?_popup=1';
    } else {
        href  += '&_popup=1';
    }
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

//Override Django js function
function dismissAddAnotherPopup(win, newId, newRepr) {
    location.reload(true);
    win.close();
}

function buildImage(image_url, alt_text, align, link) {
    if (align == 'left')
         textile = ' !<';
     else if (align == 'right')
         textile = ' !>';
     else
         textile = ' !';
     textile += image_url + '(' + alt_text + ')!';
     if (link)
         textile += ':' + link;
     return textile + ' ';
}

function buildVideoLink(video_url, title) {
    return '\n\n&& flash_video ' + video_url + ' &&\n\n'; 
}

function buildLink(link_url, title) {
    return ' "'+title+'":'+link_url+' ';
}



$(function(){
    $('#uploads li').click(function(){
        $(this).children('.popup').show();
    });
    $('.popup .close').click(function(){
        $(this).parent('.popup').hide();
        return false;
    });
    $('.popup .insert').click(function(){
        var title = $(this).attr('title');
        if ($(this).parents('.image').length) {
            var align = $(this).attr('rel');
            var link = $(this).parents('li').siblings('li.link').children('input.link').val();
            var code = buildImage(this.href, title, align, link);
        }
        else if ($(this).parents('.youtube').length) {
            var code = buildVideoLink(this.href, title);
        }
        else {
            var code = buildLink(this.href, title);
        }
        insertAtCursor(ta, code);
        $(this).parents('.popup').hide();
        return false;
    });
    $('#refresh').click(function(){
        location.reload(true);
        return false;
    });
});
