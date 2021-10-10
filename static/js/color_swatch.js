// create rgb color
function rgb(r, g, b){
    return "rgb(" + [r.toString(), g.toString(), b.toString()].join(", ") + ")";
}

// create hsl color
function hsl(h, s, l){
    return "hsl(" + [h.toString(), s.toString() + "%", l.toString() + "%"].join(", ") + ")";
}

// create brgb
function brgb(r, g, b){
    r %= 255;
    g %= 255;
    b %= 255;
    return "rgb(" + [r.toString(), g.toString(), b.toString()].join(", ") + ")";
}

// parse color space into color for css, return an array of colors that css can understand
function parseColors(data){
    var colors = [];
    $.each(data, function(index, item){
        var colorType = item.type;
        var singleColors = [];
        $.each(item.colors, function(k, v){
            singleColors.push(v);
        });
        if (typeof window[colorType] === "function") {
            var color = window[colorType](...singleColors);
            colors.push(color);
        }
    });
    return colors;
}

// render color swatch with colors
function renderColorSwatch(colors){
    $("#color-swatch").html("");
    $.each(colors, function(index, color){
        var block = '<div style="display:inline-block;width:50px;height:50px;margin:5px 5px;background-color:'+color+';"></div>'
        $("#color-swatch").append(block);
    });
}

// refresh color spaces
function refreshColorSpace(){
    $.get( "/color-spaces", function( data ) {
        var colors = parseColors(data);
        renderColorSwatch(colors);
    });
}

$( document ).ready(function(){
    refreshColorSpace();
});