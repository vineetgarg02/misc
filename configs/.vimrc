set hlsearch
set number
set ignorecase
set smartcase
colorscheme desert
set wrap

set cursorline

syntax on
au BufRead,BufNewFile *.q set filetype=sql
set runtimepath^=~/.vim/bundle/ctrlp.vim

execute pathogen#infect()
filetype plugin indent on

