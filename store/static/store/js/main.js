(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
    
})(jQuery);
function validatePassword(password) {
    // define a regex pattern to check for strong password
    var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");

    // check if password matches the pattern
    if (!strongRegex.test(password)) {
      // if not, display an error message
      document.getElementById("passwordError").innerHTML = "Password must contain at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.";
      return false;
    } else {
      // if password is strong, clear any error message
      document.getElementById("passwordError").innerHTML = "";
      return true;
    }
  }

  // add event listener to password input
  document.getElementById("password-signup").addEventListener("input", function() {
    validatePassword(this.value);
  });

  // add event listener to form submit
  document.getElementById("signupform").addEventListener("submit", function(e) {
    if (!validatePassword(document.getElementById("password-signup").value)) {
      e.preventDefault();
    }
  });

    $(document).on('click', '#suggestions-list li', function(){
        $("#search").val($(this).text());
        $(".searchForm").submit();
        });
    $(document).ready(function() {
        $("#search").on("keyup", function() {
            var searchTerm = $(this).val();
            // Make an AJAX call to the server
            $.ajax({
                type: "GET",
                url: "/search-suggestions",
                data: {search: searchTerm},
                success: function(response) {
                    var suggestionsList = $("#suggestions-list");
                    suggestionsList.empty();
                    // Show the list of suggestions
                    response.suggestions.forEach(function(suggestion) {
                        suggestionsList.append("<li>" + suggestion + "</li>");
                    });
                    $("#suggestions-list li").click(function(){
                        $("#search").val($(this).text());
                        $(".searchForm").submit();
                    });
                }
            });
        });
    });
