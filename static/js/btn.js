var btn = document.getElementById('enter');
var picked = picked_hidden.split("").reverse().join("");
var active_row = 1;

const WORDLEN = 5;
const MAXROW = 6;

function check_row(number) {
	var letters = ['', '', '', '', ''];
	var row_letters = 0;

	if (number > MAXROW)
		return;

	for (let i = 1; i <= WORDLEN; i++) {
		letters[i - 1] = document.getElementById('letter' + number + i);
		if (letters[i - 1].value) {
			row_letters += 1;
		}
	}

	// Entered all letters:
	if (row_letters == WORDLEN) {
		var guessed = 0;

		for (let i = 1; i <= WORDLEN; i++) {
			var cur = letters[i - 1];
			if (picked[i - 1] == cur.value) {
				guessed += 1;
				cur.setAttribute("style", "background-color: #90ee90");
			}
			else if (picked.includes(cur.value)) {
				cur.setAttribute("style", "background-color: #eeee90");
			}
			cur.setAttribute("disabled", "disabled");
		}
		// Guessed the wordle -> win:
		if (guessed == WORDLEN) {
			active_row = MAXROW + 1;
			return;
		}

		active_row += 1;
	}
}

btn.onclick = function() {

	if (active_row <= MAXROW) {
		check_row(active_row);
	}
	if (active_row > MAXROW) {
		btn.setAttribute("disabled", "disabled");
	}
}

document.addEventListener("DOMContentLoaded", function(event) {

  for (let j = 1; j <= MAXROW; j++) {
	for (let i = 1; i <= WORDLEN; i++) {
		lett = document.getElementById('letter' + j + i);

		if (i < WORDLEN) {
			lett.onkeyup = function() {
				if (this.value) {
					next = document.getElementById('letter' + j + (i + 1));
					next.focus();
				}
			};
		}
		else {
			lett.onkeyup = function(event) {
				if (event.keyCode == 13) {
					btn.click();
				}
			};
		}
	}
  }
});
