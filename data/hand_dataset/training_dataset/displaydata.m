function displaydata
% This function displays training data with annotations overlaid. Other
% datasets could be seen in the same way by changing the paths of image
% and annotation directories

uf = dir('training_data/images/*.jpg');
for i = 1000:length(uf)
    dot = strfind(uf(i).name,'.');
    imname = uf(i).name(1:dot-1);
    load(['training_data/annotations/' imname '.mat']);
    im = imread(['training_data/images/' uf(i).name]);
    imshow(im);
    for j = 1:length(boxes)
        box = boxes{j};
        line([box.a(2) box.b(2)]',[box.a(1) box.b(1)]','LineWidth',3,'Color','y');
        line([box.b(2) box.c(2) box.d(2) box.a(2)]',[box.b(1) box.c(1) box.d(1) box.a(1)]','LineWidth',3,'Color','r');
    end
    disp('Press any key to move onto the next image');pause;
end