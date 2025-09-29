$(document).ready(function(){
    // Dark mode toggle
    $("#toggleDark").click(function(){
        $("body").toggleClass("dark");
        $(".card").toggleClass("dark");
    });

    // Form validation
    $("#expenseForm").submit(function(e){
        let date = $("#date").val();
        let amount = $("#amount").val();
        let category = $("#category").val();
        if(!date || !amount || !category){
            e.preventDefault();
            $("#error").text("Date, Amount, and Category are required!");
        }
    });
});
