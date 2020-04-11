
//check of specific todos by clicking
$("ul").on("click", "li", function(){
    $(this).toggleClass("completed");
});

$("ul").on("click", "span",function(event){
    $(this).parent().fadeOut(500,function(){
        $(this).remove()
    });
    event.stopPropagation();
});

$("input[type='text']").keypress(function(event){
    if(event.which === 13){
       var todotext = $(this).val();
       $(this).val("");
       $('#list').append("<li><span><i class='fas fa-trash-alt rmv'></i></span> "+todotext+"</li>");
    }
})

$(".add").click(function(){
    $("input[type='text']").toggleClass("display");
});