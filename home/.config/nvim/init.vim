
"visual aid
set cursorline
set textwidth=72
set colorcolumn=+1,+10
set showmatch
set number

set laststatus=2

"want to paste from and copy to X clipboard
set clipboard=unnamedplus

" shorter timeout
set timeoutlen=50

set backspace=indent,eol,start

"Indent
set autoindent
set smartindent

set tabstop=4
set shiftwidth=4

set dir=~/tmp/nvim

let g:airline_powerline_fonts=1
let g:airline_theme='solarized'

execute pathogen#infect()

set background=dark " dark | light "
colorscheme flattened_dark
syntax enable

"NERDTree
autocmd WinEnter * call s:CloseIfOnlyNerdTreeLeft()

""""""""""
"Functions
""""""""""
" Close all open buffers on entering a window if the only
" buffer that's left is the NERDTree buffer
function! s:CloseIfOnlyNerdTreeLeft()
  if exists("t:NERDTreeBufName")
    if bufwinnr(t:NERDTreeBufName) != -1
      if winnr("$") == 1
        q
      endif
    endif
  endif
endfunction

"special mappings
set pastetoggle=<F11>
