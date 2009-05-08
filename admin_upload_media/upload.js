
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

//change the following 3 functions to insert HTML, Markdown, whatever
function buildImage(image_url, alt_text, align, link, use_html) {
    textile = ' !';
    html = '<img ';
    if (align == 'left') {
        textile += '<';
        html += 'class="left" align="left" ';
    } else if (align == 'right') {
         textile += '>';
         html += 'class="right" align="right"';
	}
    textile += image_url + '(' + alt_text + ')!';
    html += 'src="'+image_url+'" alt="'+alt_text+'" />';
    if (link) 
        textile += ':' + link;
        html = '<a href="'+link+'">'+html+'</a>';
    if (use_html)
        return html + ' ';
    else
        return textile + ' ';
}

//this needs some help via a templatetag
function buildVideoLink(video_url, title, thumb, use_html) {
    if (use_html) {
        return '<a class="flash_video" href="'+video_url+'" title="'+title+'"><img src="'+thumb+'" alt="'+title+'" /></a>';
    }
	return '\n\n&& flash_video ' + video_url + ' &&\n\n'; 
}

function buildLink(link_url, title, use_html) {
    if (use_html) {
        return ' <a href="'+link_url+'" title="'+title+'" class="image">'+title+'</a> ';
	} else {
        return ' "'+title+'":'+link_url+' ';
    }
}

function buildCode(self, use_html) {
    var title = self.attr('title');
    if (self.parents('.image').length) {
        var align = self.attr('rel');
        var link = self.parents('li').siblings('li.link').children('input.link').val();
        var code = buildImage(self.attr('href'), title, align, link, use_html);
    } else if (self.parents('.youtube').length) {
        var code = buildVideoLink(self.attr('href'), title, self.attr('rel'), use_html);
    } else {
        var code = buildLink(self.attr('href'), title, use_html);
    }
    return code;
}

$(function(){

    $('#uploads li').click(function(){
        $(this).children('.popup').show();
    });

    $('.popup .close').click(function(){
        $(this).parent('.popup').hide();
        return false;
    });
	
	// switch between different editors //
    $('.popup .insert').click(function(){
        var use_html = true;
        if (parent.TinyMCE_Engine !== undefined) {
            var mce_instance = $(ta).siblings('span').attr('id').replace('_parent','');
            tinyMCE.execCommand("mceAddControl", true, this.id);
        } else if (parent.WYMeditor !== undefined) {
    		var wym = $.wymeditors(0);
    		wym.insert(buildCode($(this), use_html));
        } else {
            use_html = false;
            insertAtCursor(ta, buildCode($(this), use_html));
        }
        $(this).parents('.popup').hide();
        return false;
    });




	//         if (parent.TinyMCE_Engine !== undefined) {
	//         	parent.tinyMCE.execInstanceCommand(mce_instance ,"mceInsertContent", false, code);
	// } else if (parent.WYMeditor !== undefined) {

    $('#all-uploads').click(function(){
        $('.image').show()
        $('.flash_video').show()
        return false;
    });
    
    $('#images').click(function(){
        $('.flash_video').hide()
        $('.image').show()
        return false;
    });
        
    $('#files').click(function(){
        $('.flash_video').show()
        $('.image').hide()
        return false;
    });
});