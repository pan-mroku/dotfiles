_tmux_session_complete()
{
		local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "`tmux_session.sh`" -- $cur) )
}
complete -F _tmux_session_complete tmux_session.sh
