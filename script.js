let board = ['', '', '', '', '', '', '', '', ''];
let markOrderX = []; // Track order for X marks (FIFO queue for X only)
let markOrderO = []; // Track order for O marks (FIFO queue for O only)
let currentPlayer = 'X';
let gameActive = true;
let scores = { X: 0, O: 0, draw: 0 };

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];

const statusDisplay = document.querySelector('.status');
const cells = document.querySelectorAll('.cell');
const restartBtn = document.getElementById('restartBtn');
const scoreX = document.getElementById('scoreX');
const scoreO = document.getElementById('scoreO');
const scoreDraw = document.getElementById('scoreDraw');

// Count marks per player on board
function countMarksForPlayer(player) {
    return board.filter(cell => cell === player).length;
}

function removeOldestMarkOfPlayer(playerToRemove) {
    const playerQueue = playerToRemove === 'X' ? markOrderX : markOrderO;
    const oldestIndex = playerQueue.shift(); // Remove first X or O placed by this player
    
    if (oldestIndex === null || oldestIndex === undefined) return;
    
    board[oldestIndex] = '';
    const cell = document.querySelector(`.cell[data-index="${oldestIndex}"]`);
    cell.textContent = '';
    cell.classList.remove(playerToRemove.toLowerCase(), 'winning');
    
    // Clear winning highlights since mark was removed
    highlightWinningCells([]);
}

function handleCellClick(clickedCellEvent) {
    const clickedCell = clickedCellEvent.target;
    const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));

    if (board[clickedCellIndex] !== '' || !gameActive) {
        return;
    }

    // Check if this player already has 3 marks on board - remove oldest of SAME type
    const currentMarksOnBoard = countMarksForPlayer(currentPlayer);
    if (currentMarksOnBoard >= 3) {
        removeOldestMarkOfPlayer(currentPlayer);
    }

    handleCellPlayed(clickedCell, clickedCellIndex);
    checkForWinner();
}

function handleCellPlayed(clickedCell, clickedCellIndex) {
    board[clickedCellIndex] = currentPlayer;
    
    // Add to player-specific queue (only add after placing the mark)
    if (currentPlayer === 'X') {
        markOrderX.push(clickedCellIndex);
    } else {
        markOrderO.push(clickedCellIndex);
    }
    
    clickedCell.textContent = currentPlayer;
    clickedCell.classList.add(currentPlayer.toLowerCase());
}

function checkForWinner() {
    if (!gameActive) return;
    
    for (let i = 0; i < winningConditions.length; i++) {
        const [a, b, c] = winningConditions[i];
        
        if (board[a] !== '' && board[b] !== '' && board[c] !== '') {
            // All three positions are filled - check if same player owns them
            if (board[a] === board[b] && board[b] === board[c]) {
                statusDisplay.textContent = `Player ${currentPlayer} wins! 🎉`;
                gameActive = false;
                updateScore(currentPlayer);
                highlightWinningCells([a, b, c]);
                return;
            }
        }
    }
    
    handlePlayerChange();
}

function handlePlayerChange() {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    
    const xCount = countMarksForPlayer('X');
    const oCount = countMarksForPlayer('O');
    
    if (xCount < 3 && oCount < 3) {
        statusDisplay.textContent = `Player ${currentPlayer}'s turn`;
    } else {
        if (xCount === 3) {
            statusDisplay.textContent = `Player ${currentPlayer}'s turn (X has max marks, will vanish on next X)`;
        } else if (oCount === 3) {
            statusDisplay.textContent = `Player ${currentPlayer}'s turn (O has max marks, will vanish on next O)`;
        } else {
            statusDisplay.textContent = `Player ${currentPlayer}'s turn`;
        }
    }
}

function highlightWinningCells(cells) {
    cells.forEach(index => {
        document.querySelector(`.cell[data-index="${index}"]`).classList.add('winning');
    });
}

function updateScore(result) {
    if (result === 'X') {
        scores.X++;
    } else if (result === 'O') {
        scores.O++;
    } else {
        scores.draw++;
    }
    scoreX.textContent = scores.X;
    scoreO.textContent = scores.O;
    scoreDraw.textContent = scores.draw;
}

function handleRestartGame() {
    gameActive = true;
    currentPlayer = 'X';
    board = ['', '', '', '', '', '', '', '', ''];
    markOrderX = [];
    markOrderO = [];
    statusDisplay.textContent = `Player X's turn`;
    
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o', 'winning');
    });
}

cells.forEach(cell => cell.addEventListener('click', handleCellClick));
restartBtn.addEventListener('click', handleRestartGame);
