var btn = document.getElementById('enter');
var stats_modal = document.getElementById('statistics_modal');
var stats_mbody = stats_modal.getElementsByClassName('modal-body')[0];
var stats_mclose = stats_modal.getElementsByTagName('button');

var picked = picked_hidden.split("").reverse().join("");
var game_status = "init";

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

const alphabet = "йцукенгґшщзхїфівапролджєячсмитьбю";
var alphabit   = "111111111111111111111111111111111";

const clid = "yirdle-clid";

var active_row = 1;

var initial_state = {
    row_index: 0,
    solution: null,
    game_status: game_status,
    games_played: 0,
    last_played: null,
    last_completed: null,
    last_completed_fmt: "",
    cur_streak: 0,
    board_state: null,
};

function objectify(cookie) {
	var ck;
	var now = new Date();

	if (cookie == null)
	    ck = new Object();
	else
	    ck = cookie;

	ck.row_index = active_row;
	ck.game_status = game_status;
	if (game_status == "win" || game_status == "loss") {
		if (ck.solution != picked) {
			ck.games_played += 1;
			ck.cur_streak += (game_status == "win");
		}
		ck.solution = picked;
	}
	ck.last_played = new Date();
	if (game_status == "win") {
		ck.last_completed = now;
		ck.last_completed_fmt = now.toLocaleDateString('en-US', {
			year: 'numeric',
			month: 'long',
			day: 'numeric',
			hour: 'numeric',
			minute: 'numeric',

		 });
	}
	if (game_status == "loss") {
		ck.cur_streak = 0;
	}

	ck.board_state = store_board_state();

	return ck;
}

function get_cookie() {
    var data = window.localStorage.getItem(clid);

    if (data == null)
    	data = JSON.stringify(initial_state);

    return JSON.parse(data);
}

function set_cookie() {
    var cookie = get_cookie();
    ! function(data) {
    	window.localStorage.setItem(clid, JSON.stringify(data))
    } (objectify(cookie));
}

function disable_rows(current_row) {
	for (let i = current_row + 1; i <= MAXROW; i++) {
		for (let j = 1; j <= WORDLEN; j++) {
			letter = document.getElementById('letter' + i + j);
			letter.setAttribute("disabled", "disabled");
		}
	}
}

function store_board_state() {
	var board_state = new Array(MAXROW * WORDLEN);

	for (let i = 1; i <= MAXROW; i++) {
		for (let j = 1; j <= WORDLEN; j++) {
			board_state[(i - 1) * WORDLEN + (j - 1)] = document.getElementById('letter' + i + j).value;
		}
	}
	return board_state;
}

function restore_board_state() {
	var ck = get_cookie();
	var letter;

	if (ck.board_state == null)
		return;

	for (let i = 1; i <= MAXROW; i++) {
		for (let j = 1; j <= WORDLEN; j++) {
			letter = document.getElementById('letter' + i + j);
			letter.value = ck.board_state[(i - 1) * WORDLEN + (j - 1)];
		}
		check_row(i);
	}
}

function draw_keyboard() {
	const row_1st = 13;
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
	var letters = [];
	var word = [];
	var row_letters = 0;
	var guessed = 0;
	var cur = {};
	var key_status = KEY_INITIAL;

	if (number > MAXROW)
		return;

	for (let i = 1; i <= WORDLEN; i++) {
		letters[i - 1] = document.getElementById('letter' + number + i);
		if (letters[i - 1].value) {
			word[row_letters] = letters[i - 1].value;
			row_letters += 1;
		}
	}

	// Entered all letters:
	if (row_letters == WORDLEN) {
		word = word.join("");

		if (!word_list.includes(word)) {
			btn.classList.add("apply-shake");
			return;
		}

		for (let i = 1; i <= WORDLEN; i++) {
			cur = letters[i - 1];

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
			btn.setAttribute("disabled", "disabled");
			disable_rows(active_row);
			game_status = "win";
			return;
		}
		else if (active_row == MAXROW) {
			btn.innerHTML = '<b>Поразка</b>';
			btn.setAttribute("style", "background-color: " + t_bgcolors[KEY_INACTIVE]);
			btn.setAttribute("disabled", "disabled");
			game_status = "loss";
		}

		active_row += 1;
	}
}

btn.onclick = function() {

	if (game_status == "init" || game_status == "running") {
		game_status = "running";
		check_row(active_row);
		set_cookie();
		draw_keyboard();
	}
	if (game_status == "win" || game_status == "loss") {
		set_cookie();
		stats_modal_show(game_status);
	}
}

btn.onanimationend = function(event) {
	btn.classList.remove("apply-shake");
}

function stats_modal_hide() {
	stats_modal.classList.remove('show');
	stats_modal.classList.remove('in');
}

function stats_modal_show(game_status) {
	var ck = get_cookie();
	var summary = (game_status == 'win') ? '<b>Solved today\'s wordle</b>' : '<b>Lost today</b>';

	stats_mbody.innerHTML = summary + '<br><b>Row:</b> ' + ck.row_index + '<br><b>Time:</b> ' + ck.last_completed_fmt + '<br><b>Streak:</b> ' + ck.cur_streak;
	stats_modal.classList.add('show');
	stats_modal.classList.add('in');
}

stats_mclose[0].onclick = stats_modal_hide;

document.addEventListener("DOMContentLoaded", function(event) {

	for (let j = 1; j <= MAXROW; j++) {
		for (let i = 1; i <= WORDLEN; i++) {
			lett = document.getElementById('letter' + j + i);
			lett.setAttribute("autocomplete", "chrome-off");

			lett.onkeydown = function(event) {
				// Handle Backspace key
				if (event.keyCode == 8) {
					if (this.value)
						this.value = '';
					else {
						if (i > 1) {
							prev = document.getElementById('letter' + j + (i - 1));
							prev.focus();
						}
					}
				}
			};

			lett.oninput = function(event) {
				if (i < WORDLEN && this.value) {
					next = document.getElementById('letter' + j + (i + 1));
					next.focus();
				}
			};

			lett.onkeyup = function(event) {
				// Enter key
				if (i == WORDLEN && event.keyCode == 13) {
					btn.click();
				}
			};
		}
	}

	draw_keyboard();

	var ck = get_cookie();

	if (ck.solution == picked) {
		restore_board_state();
		stats_modal_show(ck.game_status);
	}

});
