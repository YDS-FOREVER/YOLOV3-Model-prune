function counttraindata
%This function gives the statistics of the training data
datasets = {'Buffy','Inria','Poselet','Skin','VOC2007','VOC2010'};
datasets_fullname = {'Buffy stickman                                                 ','INRIA pedestrian                                               ', 'Poselet (H3D)                                                  ', 'Skin dataset                                                   ', 'PASCAL VOC 2007 training and validation set                    ','PASCAL VOC 2010 train and val set (except human layout val set)'};
count = zeros(6,1);
countimg = zeros(6,1);
countbig = zeros(6,1);
uf = dir('training_data/annotations/*.mat');
for i = 1:length(uf)
    dot = strfind(uf(i).name,'.');
    imname = uf(i).name(1:dot-1);
    underscore = strfind(uf(i).name,'_');
    datasource_name = uf(i).name(1:underscore-1);
    index_cmp = strcmp(datasets,datasource_name);
    I = find(index_cmp > 0);
    flag = 0;
    im = imread(sprintf('training_data/images/%s.jpg',imname));
    load(sprintf('training_data/annotations/%s',uf(i).name));
    [h w d] = size(im);
    for j = 1:length(boxes)
        count(I) = count(I) + 1;
        [truea, trueb, truec, trued] = getBox(boxes,j);
        angle = 180*atan2(truea(1)-trueb(1),trueb(2)-truea(2))/pi;
        segh = (truea(1)-trued(1))*(truea(1)-trued(1))+(truea(2)-trued(2))*(truea(2)-trued(2));
        segw = (truea(1)-trueb(1))*(truea(1)-trueb(1))+(truea(2)-trueb(2))*(truea(2)-trueb(2));
        segh = round(sqrt(segh)); segw = round(sqrt(segw));
        ta = ptRotate(truea,angle,h,w);
        xmin = ta(2); ymin = ta(1);
        xmax = ta(2) + segw; ymax = ta(1) + segh;
        area = (xmax-xmin+1)*(ymax-ymin+1);
        if(area > 1500)
            flag = 1;
            countbig(I) = countbig(I) + 1;
        end
    end
    if(flag == 1)
        countimg(I) = countimg(I) + 1;
    end
end
fprintf('                                                               \t #All\t #Big\t #Images having big hands\n');

for i = 1:length(count)
    fprintf('%s\t %d\t %d\t %d\n',datasets_fullname{i},count(i),countbig(i),countimg(i));
end                

fprintf('Total                                                          \t %d\t %d\t %d\n',sum(count),sum(countbig),sum(countimg));


function [a, b, c, d] = getBox(boxes,segNr)
a = boxes{segNr}.a;
b = boxes{segNr}.b;
c = boxes{segNr}.c;
d = boxes{segNr}.d;

% Rotate point 'p' by 'angle' around (h/2,w/2), i.e. the image centre
function tp = ptRotate(p,angle,h,w)

angle = angle*pi/180;
tp(1) = p(2)*sin(angle)+p(1)*cos(angle)+h/2-w/2*sin(angle)-h/2*cos(angle);
tp(2) = p(2)*cos(angle)-p(1)*sin(angle)+w/2-w/2*cos(angle)+h/2*sin(angle);
tp(1) = round(tp(1)); tp(2) = round(tp(2));