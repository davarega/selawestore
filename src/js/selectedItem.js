let selectedDiv = null;

function toggleSelect(divNumber) {
	const divs = document.querySelectorAll('.interactive-div');
	divs.forEach((div, index) => {
		if (index + 1 === divNumber) {
			// if (selectedDiv === divNumber) {
			// 	// If clicking the same div, deselect it
			// 	div.classList.remove('selected-item');
			// 	selectedDiv = null;
			// } else {
			// 	// Select the new div
			// 	div.classList.add('selected-item');
			// 	selectedDiv = divNumber;
			// }
			div.classList.add('selected-item');
			selectedDiv = divNumber;
		} else {
			// Deselect all other divs
			div.classList.remove('selected-item');
		}
	});
}