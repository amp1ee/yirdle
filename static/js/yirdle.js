var btn = document.getElementById('enter');
var picked = picked_hidden.split("").reverse().join("");
var active_row = 1;

const WORDLEN = 5;
const MAXROW = 6;

const KEY_INACTIVE = 0;
const KEY_INITIAL = 1;
const KEY_SPOTON = 2;
const KEY_INWORD = 3;

const t_bgcolors = [
	'#ee9090',
	'#ddddcc',
	'#90ee90',
	'#eeee90'
];

const alphabet = "йцукенгшщзхїфівапролджєячсмитьбю";
var alphabit   = "11111111111111111111111111111111";

function draw_keyboard() {
	const row_1st = 12;
	const row_2nd = row_1st + 11;
	const row_3rd = row_2nd + 9;

	var keyboard = document.getElementById("keyboard");

	var row1, row2, row3;

	row1 = document.getElementById("row1");
	row2 = document.getElementById("row2");
	row3 = document.getElementById("row3");

	if (row1 == null) {
		row1 = document.createElement("div");
		row1.classList.add("row");
		row1.id = "row1";

		row2 = document.createElement("div");
		row2.classList.add("row");
		row2.id = "row2";
		row2.setAttribute("style", "margin-left: 10px");

		row3 = document.createElement("div");
		row3.classList.add("row");
		row3.id = "row3";
		row3.setAttribute("style", "margin-left: 20px");

		keyboard.appendChild(row1);
		keyboard.appendChild(row2);
		keyboard.appendChild(row3);
	}

	while (row1.firstChild) {
		row1.removeChild(row1.firstChild);
	}
	while (row2.firstChild) {
		row2.removeChild(row2.firstChild);
	}
	while (row3.firstChild) {
		row3.removeChild(row3.firstChild);
	}

	var i = 0;
	var cur_row = 1;

	for (const letter of alphabet.split("")) {

		key = document.createElement("div");
		key.classList.add('col');

		key_in = document.createElement("input");
		key_in.setAttribute("type", "text");
		key_in.setAttribute("size", "1");
		key_in.setAttribute("readonly", "");
		key_in.value = letter;

		var key_status = alphabit.split("")[i];
		key.setAttribute("style", "background-color: " + t_bgcolors[key_status]);
		key.appendChild(key_in);

		if (i < row_1st) {
			row1.appendChild(key);
		} else if (i < row_2nd) {
			row2.appendChild(key);
		} else if (i < row_3rd) {
			row3.appendChild(key);
		}
		i++;
	}

}

function mark_letter(marked_letter, type) {

	var i = 0;

	arr_alphabit = alphabit.split("");

	for (var l of alphabet.split("")) {
		if (l == marked_letter && arr_alphabit[i] != KEY_SPOTON) {
			arr_alphabit[i] = type.toString();
		}
		i++;
	}

	alphabit = arr_alphabit.join("");
}

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
		var key_status = KEY_INITIAL;

		for (let i = 1; i <= WORDLEN; i++) {
			var cur = letters[i - 1];

			if (picked[i - 1] == cur.value) {
				guessed += 1;
				key_status = KEY_SPOTON;
			}
			else if (picked.includes(cur.value)) {
				key_status = KEY_INWORD;
			}
			else {
				key_status = KEY_INACTIVE;
			}
			mark_letter(cur.value, key_status);

			cur.setAttribute("disabled", "disabled");
			if (key_status != KEY_INACTIVE) {
				cur.setAttribute("style", "background-color: " + t_bgcolors[key_status]);
			}
		}

		if (guessed == WORDLEN) {
			btn.innerHTML = '<b>Перемога!</b>';
			btn.setAttribute("style", "background-color: " + t_bgcolors[KEY_SPOTON]);
			active_row = MAXROW + 1;
			return;
		}
		else if (active_row == MAXROW) {
			btn.innerHTML = '<b>Поразка</b>';
			btn.setAttribute("style", "background-color: " + t_bgcolors[KEY_INACTIVE]);
		}

		active_row += 1;
	}
}

btn.onclick = function() {

	if (active_row <= MAXROW) {
		check_row(active_row);
		draw_keyboard();
	}
	if (active_row > MAXROW) {
		btn.setAttribute("disabled", "disabled");
	}
}

document.addEventListener("DOMContentLoaded", function(event) {

	for (let j = 1; j <= MAXROW; j++) {
		for (let i = 1; i <= WORDLEN; i++) {
			lett = document.getElementById('letter' + j + i);
			lett.setAttribute("autocomplete", "chrome-off");

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

	draw_keyboard();

});
