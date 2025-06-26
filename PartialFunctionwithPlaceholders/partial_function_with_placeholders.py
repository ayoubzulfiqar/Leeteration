_ = object()

def partial_with_placeholders(func, *args_with_placeholders, **kwargs_with_placeholders):
    def new_partial_func(*new_args, **new_kwargs):
        filled_args = []
        new_args_iter = iter(new_args)

        placeholder_pos_count = 0
        for arg_val in args_with_placeholders:
            if arg_val is _:
                placeholder_pos_count += 1
                try:
                    filled_args.append(next(new_args_iter))
                except StopIteration:
                    raise TypeError(
                        f"Not enough positional arguments provided to fill all {placeholder_pos_count} placeholders. "
                        f"Missing {placeholder_pos_count - len(new_args)} argument(s)."
                    )
            else:
                filled_args.append(arg_val)

        remaining_new_args = list(new_args_iter)
        if remaining_new_args:
            raise TypeError(
                f"Too many positional arguments provided. Expected {placeholder_pos_count} for placeholders, "
                f"but got {len(new_args)}. Extra arguments: {remaining_new_args}"
            )

        final_kwargs = kwargs_with_placeholders.copy()

        for kw, val in new_kwargs.items():
            if kw in final_kwargs:
                if final_kwargs[kw] is _:
                    final_kwargs[kw] = val
                else:
                    raise TypeError(f"Keyword argument '{kw}' is already fixed and not a placeholder.")
            else:
                final_kwargs[kw] = val

        unfilled_kw_placeholders = [kw for kw, val in final_kwargs.items() if val is _]
        if unfilled_kw_placeholders:
            raise TypeError(f"Missing values for keyword placeholders: {', '.join(unfilled_kw_placeholders)}")

        return func(*filled_args, **final_kwargs)
    return new_partial_func