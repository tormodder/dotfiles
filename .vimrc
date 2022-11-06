" Set the background to dark
set background=dark

" Enable line numbers
set number

" Set ruler at 80
set cc=78

" Vim plug begin
call plug#begin()
" Default directory: ~/.vim/plugged

" Add pathfinder plugin
"if has('python3') && has('timers')
"  Plug 'danth/pathfinder.vim'
"else
"  echoerr 'pathfinder.vim is not supported on this Vim installation'
"endif

" Install Gruvbox theme
if (has("termguicolors"))
    set termguicolors
endif
Plug 'morhetz/gruvbox'


call plug#end()

" Add gruvbox colorscheme
let g:gruvbox_italics=1
colorscheme gruvbox

