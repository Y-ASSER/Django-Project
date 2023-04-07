

function loadHomePage(){
    $.ajax({
      url: '/app/index/home/',
      method: 'GET',
      success: function(data) {
        const myDiv = document.querySelector('#detailsDiv');
        myDiv.innerHTML = data;
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log(textStatus + ': ' + errorThrown);
      }
    });
  }

    function loadAttendancePage(){
      $.ajax({
        url: '/app/index/attendance/',
        method: 'GET',
        success: function(data) {
          const myDiv = document.querySelector('#detailsDiv');
          myDiv.innerHTML = data;
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log(textStatus + ': ' + errorThrown);
        }
      });
    }

