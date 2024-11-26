import fitz

def add_frame(input_pdf_path, output_pdf_path):

    """
    Add a rectangle frame to each page of a PDF document.
    :param input_pdf_path: Path to the input PDF file
    :param output_pdf_path: Path to save the output PDF file
    :param frame_padding: Width of the frame in points (default: 20)
    """
    
    try:
        doc = fitz.open(input_pdf_path)
        
        for page_num in range(len(doc)):
            page = doc[page_num]
            
            page_rect = page.rect

            frame_padding = 20
            
            frame_rect = fitz.Rect(
                frame_padding,                    # left
                frame_padding,                    # top
                page_rect.width - frame_padding,  # right
                page_rect.height - frame_padding  # bottom
            )
            
            page.draw_rect(
                frame_rect,           # rectangle coordinates
                width = 2             # frame thickness
            )
        
        doc.save(output_pdf_path)
        
        print(f"PDF with rectangle frame saved to {output_pdf_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'doc' in locals():
            doc.close()


input_pdf = 'r.pdf'
output_pdf = 'output.pdf'

add_frame(input_pdf, output_pdf)