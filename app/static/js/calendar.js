function loadCalendar()
{
    debugger;
    //$(".calendar").prepend('<div class="added">This is added div </div>');
    const today = new Date();
    const year = today.getFullYear();
    const month = today.getMonth();
    const numDays = new Date(year, month + 1, 0).getDate();
    const firstDay = new Date(year, month, 1).getDay();
    let dayCount = 1;

    for (let i = 0; i < 6; i++) {
        document.write('<tr>');
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                document.write('<td></td>');
            } else if (dayCount > numDays) {
                document.write('<td></td>');
            } else {
                if (year === today.getFullYear() && month === today.getMonth() && dayCount === today.getDate()) {
                    document.write('<td class="today">' + dayCount + '</td>');
                } else {
                    document.write('<td>' + dayCount + '</td>');
                }
                dayCount++;
            }
        }
        document.write('</tr>');
    }
}

window.onload = (event) => {
    debugger;
    $("#calendar").ready( function() {
		debugger;
		//loadCalendar();
	})
  };