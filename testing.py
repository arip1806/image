def create_canvas_draw_instance(background_image, key, height, width): 

    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0)",  
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        background_image=Image.open(background_image),
        update_streamlit=realtime_update,
        drawing_mode=drawing_mode,
        height = height, 
        width = width,
        key=key,
    )

    return canvas_result
