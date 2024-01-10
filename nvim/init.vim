set number
set background=dark
set termguicolors
set autoindent
set tabstop=2
set shiftwidth=2

call plug#begin('~/.local/share/nvim/plugged')

Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'shaunsingh/nord.nvim'
Plug 'shaunsingh/moonlight.nvim'
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug '/jmcantrell/vim-virtualenv'
Plug '/tpope/vim-fugitive'
call plug#end()

colorscheme nord

let mapleader=","
"Map keys for tabs
map <leader>tn :tabnew<cr>
map <leader>t  :tabnext
map <leader>tm :tabmove
map <leader>tc :tabclose<cr>
map <leader>to :tabonly<cr>
"map keys for windows
map <leader>f  :split
map <leader>e  :vsplit
"open NERDTree
map <C-o> :NERDTreeToggle %<CR>

let g:airline_theme='atomic'
if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif

"set symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''

"autoclose {}
inoremap { {}<left>
